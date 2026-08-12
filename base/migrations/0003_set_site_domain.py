from django.conf import settings
from django.db import migrations


def set_site_domain(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            'domain': settings.SITE_DOMAIN,
            'name': 'CollabStudy',
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_avatar'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(set_site_domain, migrations.RunPython.noop),
    ]
