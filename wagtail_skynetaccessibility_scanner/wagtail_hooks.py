from django.urls import path, include, reverse_lazy
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from . import urls as scanner_urls


@hooks.register('register_admin_urls')
def register_scanner_urls():
    return [
        path('skynet-scanner/', include(scanner_urls)),
    ]


@hooks.register('register_admin_menu_item')
def register_scanner_menu_item():
    return MenuItem(
        'SkynetAccessibility Scanner',
        reverse_lazy('wagtail_skynetaccessibility_scanner:dashboard'),
        order=10000,
    )
