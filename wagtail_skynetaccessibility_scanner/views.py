from django.shortcuts import redirect, render

from .models import WagtailSkynetScannerSettings


def scanner_dashboard(request):
    """Wagtail admin panel view for the Skynet Accessibility Scanner."""
    scheme = 'https' if request.is_secure() else 'http'
    host   = request.get_host().split(':')[0]
    domain = f'{scheme}://{host}'

    cfg = WagtailSkynetScannerSettings.objects.first()

    if request.method == 'POST':
        domain_val = request.POST.get('website_domain', '').strip()
        if cfg:
            cfg.website_domain = domain_val
            cfg.save()
        return redirect(request.path)

    context = {
        'domain':     domain,
        'website_id': cfg.website_id if cfg else '',
    }
    return render(request, 'wagtail_skynetaccessibility_scanner/dashboard.html', context)
