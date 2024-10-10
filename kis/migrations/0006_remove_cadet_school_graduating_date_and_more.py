# Generated by Django 5.0.4 on 2024-10-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kis', '0005_alter_punishment_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='school_graduating_date',
        ),
        migrations.AddField(
            model_name='cadet',
            name='school_graduating_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='School graduating year'),
        ),
    ]
