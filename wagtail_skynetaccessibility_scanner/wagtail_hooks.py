from django.urls import path, include, reverse_lazy
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from . import urls as scanner_urls


@hooks.register('register_admin_urls')
def register_scanner_urls():
    return [
        path('skynet-scanner/', include(scanner_urls)),
    ]


@hooks.register('register_icons')
def register_scanner_icons(icons):
    # Adds the Skynet logo to Wagtail's icon sprite as "skynet-scanner".
    return icons + ['wagtail_skynetaccessibility_scanner/icons/skynet-scanner.svg']


@hooks.register('register_admin_menu_item')
def register_scanner_menu_item():
    return MenuItem(
        'SkynetAccessibility Scanner',
        reverse_lazy('wagtail_skynetaccessibility_scanner:dashboard'),
        icon_name='skynet-scanner',
        order=10000,
    )
