# This migration is a compatibility shim.
#
# A previous release of wagtail_skynetaccessibility_scanner introduced a
# `user_email` field in migration 0002, then removed it in 0003.  The current
# release consolidates everything into 0001_initial (the field was never part
# of the public model API), so 0002 and 0003 are kept as no-ops purely to
# satisfy Django's migration graph validator when upgrading from the old
# release.  On a fresh installation these migrations apply instantly and have
# no effect.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_skynetaccessibility_scanner', '0001_initial'),
    ]

    operations = [
        # Field was added here in the old release; it is already absent from
        # 0001_initial in this release, so nothing needs to be done.
    ]
