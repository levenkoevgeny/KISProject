# Generated by Django 5.0.4 on 2024-10-10 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kis', '0006_remove_cadet_school_graduating_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentOrgan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(max_length=255, verbose_name='Комплектующий орган')),
                ('component_short_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Комплектующий орган (короткое название)')),
            ],
            options={
                'verbose_name': 'Комплектующий орган',
                'verbose_name_plural': 'Комплектующие органы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CountryRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_region', models.CharField(max_length=255, verbose_name='Область (страны)')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Области',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=255, verbose_name='Вид учреждения образования')),
            ],
            options={
                'verbose_name': 'Вид учреждения образования',
                'verbose_name_plural': 'Виды учреждения образования',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(max_length=255, verbose_name='Уровень образования')),
            ],
            options={
                'verbose_name': 'Уровень образования',
                'verbose_name_plural': 'Уровни образования',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='EducationLocalityKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_location_kind', models.CharField(max_length=255, verbose_name='Вид населенного пункта при получения среднейго образования')),
            ],
            options={
                'verbose_name': 'Вид населенного пункта при получения среднейго образования',
                'verbose_name_plural': 'Виды населенного пункта при получения среднейго образования',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='EntranceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrance_category_name', models.CharField(max_length=255, verbose_name='Категория поступающего')),
            ],
            options={
                'verbose_name': 'Категория поступающих',
                'verbose_name_plural': 'Категории поступающих',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='GO_ROVD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('go_rovd_name', models.CharField(max_length=255, verbose_name='ГО-РОВД')),
            ],
            options={
                'verbose_name': 'ГО-РОВД',
                'verbose_name_plural': 'ГО-РОВД',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='MilitaryOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('military_office', models.CharField(max_length=255, verbose_name='Военкомат')),
            ],
            options={
                'verbose_name': 'Военкомат',
                'verbose_name_plural': 'Военкоматы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='OrderOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_owner', models.CharField(max_length=255, verbose_name='Чей приказ')),
            ],
            options={
                'verbose_name': 'Чей приказ',
                'verbose_name_plural': 'Чьи приказы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='SocialStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_status', models.CharField(max_length=255, verbose_name='Социальный статус')),
            ],
            options={
                'verbose_name': 'Социальный статус',
                'verbose_name_plural': 'Социальные статусы',
                'ordering': ('id',),
            },
        ),
        migrations.RemoveField(
            model_name='cadet',
            name='group',
        ),
        migrations.RemoveField(
            model_name='punishment',
            name='punishment_extra_data',
        ),
        migrations.AddField(
            model_name='cadet',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.subdivision'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_expiration_extra_data',
            field=models.TextField(blank=True, null=True, verbose_name='Фабула о снятии'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_expiration_order_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приказа окончания взыскания'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_expiration_order_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер приказа окончания взыскания'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_start_extra_data',
            field=models.TextField(blank=True, null=True, verbose_name='Фабула о наложении'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_start_order_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приказа наложения взыскания'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_start_order_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер приказа наложения взыскания'),
        ),
        migrations.AlterField(
            model_name='passportissueauthority',
            name='passport_issue_authority',
            field=models.TextField(unique=True, verbose_name='Орган выдачи паспорта'),
        ),
        migrations.AlterField(
            model_name='punishment',
            name='punishment_cadet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.cadet', verbose_name='На кого'),
        ),
        migrations.AlterField(
            model_name='punishment',
            name='punishment_expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания действия взыскания'),
        ),
        migrations.AlterField(
            model_name='punishment',
            name='punishment_kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.punishmentkind', verbose_name='Вид взыскания'),
        ),
        migrations.AlterField(
            model_name='punishment',
            name='punishment_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала действия взыскания'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='rank',
            field=models.CharField(max_length=20, unique=True, verbose_name='Звание'),
        ),
        migrations.AlterField(
            model_name='rankhistory',
            name='rank_date',
            field=models.DateField(blank=True, null=True, verbose_name='С какого числа присвоено звание'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_name',
            field=models.TextField(unique=True, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='parent_subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kis.subdivision', verbose_name='Родительское подразделение'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='subdivision_name',
            field=models.CharField(max_length=255, verbose_name='Название подразделения'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='subdivision_short_name',
            field=models.CharField(max_length=30, verbose_name='Название подразделения (короткое)'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='school_kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.education', verbose_name='Вид учреждения образования'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_expiration_order_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='punishment_expiration_order_owner', to='kis.orderowner', verbose_name='Чей приказ'),
        ),
        migrations.AddField(
            model_name='punishment',
            name='punishment_start_order_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.orderowner', verbose_name='Чей приказ'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
