# Generated by Django 5.0.4 on 2024-10-16 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kis', '0017_rename_mvd_military_service_end_mvdservice_mvd_service_end'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encouragement',
            old_name='encouragement_cadet',
            new_name='cadet',
        ),
        migrations.RenameField(
            model_name='punishment',
            old_name='punishment_cadet',
            new_name='cadet',
        ),
    ]
