# Compatibility shim — see 0002_add_user_email.py for full explanation.
#
# The old release removed the `user_email` field (and possibly renamed
# others) in this migration.  Since the current release's 0001_initial
# already reflects the final schema, there is nothing to do here.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_skynetaccessibility_scanner', '0002_add_user_email'),
    ]

    operations = [
        # Removal / rename operations from the old release are no-ops here
        # because 0001_initial already targets the final schema.
    ]
