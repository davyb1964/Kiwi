# Generated by Django 2.0.6 on 2018-06-29 21:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tcms.core.contrib.auth', '0002_increase_activation_key_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserActivateKey',
            new_name='UserActivationKey',
        ),
        migrations.AlterModelTable(
            name='useractivationkey',
            table=None,
        ),
    ]
