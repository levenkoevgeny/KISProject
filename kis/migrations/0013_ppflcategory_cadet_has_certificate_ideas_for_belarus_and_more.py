# Generated by Django 5.0.4 on 2024-10-15 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kis', '0012_graduatewithhonorscategory_vpkcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PPFLCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='ППФЛ категория')),
            ],
            options={
                'verbose_name': 'ППФЛ категория',
                'verbose_name_plural': 'ППФЛ категории',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='cadet',
            name='has_certificate_ideas_for_Belarus',
            field=models.BooleanField(default=False, verbose_name='Сертификат 100 идей для Беларуси'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='has_certificate_kind_heart',
            field=models.BooleanField(default=False, verbose_name='Сертификат Доброе сердце'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='has_conviction',
            field=models.BooleanField(default=False, verbose_name='Имеет судимость'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='has_dactocard',
            field=models.BooleanField(default=False, verbose_name='Имеет дактокарту'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='has_employee_in_family',
            field=models.BooleanField(default=False, verbose_name='Имеет сотрудников в семье'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='has_gusb_check',
            field=models.BooleanField(default=False, verbose_name='Имеет проверку ГУСБ'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='health_group',
            field=models.IntegerField(blank=True, null=True, verbose_name='Группа здоровья'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Является сотрудником'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='is_orphan',
            field=models.BooleanField(default=False, verbose_name='Сирота'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='is_risk_group',
            field=models.BooleanField(default=False, verbose_name='Группа риска'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='medical_age_group',
            field=models.IntegerField(blank=True, null=True, verbose_name='Медико-возрастная группа'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='military_service_end',
            field=models.DateField(blank=True, null=True, verbose_name='Служба в армии (окончание)'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='military_service_start',
            field=models.DateField(blank=True, null=True, verbose_name='Служба в армии (начало)'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='mvd_service_end',
            field=models.DateField(blank=True, null=True, verbose_name='Служба в МВД (окончание)'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='mvd_service_start',
            field=models.DateField(blank=True, null=True, verbose_name='Служба в МВД (начало)'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='needs_increased_attention',
            field=models.BooleanField(default=False, verbose_name='Требует повышенного внимания'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='needs_psychological_support',
            field=models.BooleanField(default=False, verbose_name='Требует психологического сопровождения'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='ppfl_test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.ppflcategory', verbose_name='ППФЛ категория'),
        ),
    ]
