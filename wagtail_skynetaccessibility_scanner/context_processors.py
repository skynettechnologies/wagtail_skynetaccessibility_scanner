def skynet_scanner(request):
    scheme = 'https' if request.is_secure() else 'http'
    host   = request.get_host().split(':')[0]
    return {'SKYNET_DOMAIN_URL': f'{scheme}://{host}'}
