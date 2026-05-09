import ipaddress

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import WagtailSkynetScannerSettings

INVALID_HOSTS = {'localhost', '127.0.0.1', '::1', '0.0.0.0'}


def get_invalid_domain_message(host):
    base = f'"{host}" is not a valid domain. Please use your public domain name.'
    if host.lower() in INVALID_HOSTS:
        return base
    try:
        ip = ipaddress.ip_address(host)
        if ip.is_loopback or ip.is_private or ip.is_unspecified:
            return f'IP addresses and local hosts are not supported. {base}'
    except ValueError:
        pass
    return None


def scanner_dashboard(request):
    """Wagtail admin panel view for the Skynet Accessibility Scanner."""
    scheme = 'https' if request.is_secure() else 'http'
    host   = request.get_host().split(':')[0]
    domain = f'{scheme}://{host}'

    invalid_domain_message = get_invalid_domain_message(host)
    cfg = WagtailSkynetScannerSettings.objects.first()

    if request.method == 'POST':
        domain_val = request.POST.get('website_domain', '').strip()
        if cfg:
            cfg.website_domain = domain_val
            cfg.save()
        return redirect(request.path)

    context = {
        'cfg':                    cfg,
        'domain':                 domain,
        'website_id':             cfg.website_id if cfg else '',
        'csrf_token':             get_token(request),
        'invalid_domain_message': invalid_domain_message,
    }
    return render(request, 'wagtail_skynetaccessibility_scanner/dashboard.html', context)


# ── Live user-info endpoint ───────────────────────────────────────────────────
# The browser JS calls this endpoint to get the currently-logged-in Wagtail
# admin's credentials.  Returns the user's real email when available so the JS
# can decide whether to show or hide the "Add Email" toggle:
#   • real email present  → hide the toggle (user already has one)
#   • no email / no-reply placeholder → show the toggle so they can add one
@login_required
def user_info(request):
    """Return the logged-in Wagtail user's profile as JSON."""
    user = request.user

    # Resolve the best available email.
    # Wagtail stores the email on the standard Django auth User model.
    email = (getattr(user, 'email', '') or '').strip()

    # A missing or placeholder address counts as "no real email".
    has_real_email = bool(email) and not email.lower().startswith('no-reply@')

    full_name = (
        getattr(user, 'get_full_name', lambda: '')()
        or getattr(user, 'first_name', '')
        or getattr(user, 'username', '')
        or ''
    ).strip()

    return JsonResponse({
        'id':             user.pk,
        'name':           full_name,
        'email':          email,
        'username':       getattr(user, 'username', ''),
        # Convenience flag so JS can decide instantly without string-checking
        'has_real_email': has_real_email,
    })

