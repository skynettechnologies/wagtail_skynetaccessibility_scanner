from django.apps import AppConfig


class WagtailSkynetScannerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wagtail_skynetaccessibility_scanner'
    verbose_name = 'Skynet Accessibility Scanner'

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(_create_default_settings, sender=self)


def _create_default_settings(sender, **kwargs):
    try:
        from .models import WagtailSkynetScannerSettings
        if not WagtailSkynetScannerSettings.objects.exists():
            WagtailSkynetScannerSettings.objects.create()
            print('[WagtailSkynetScanner] Default settings record created.')
    except Exception as e:
        print(f'[WagtailSkynetScanner] Could not create default settings: {e}')
