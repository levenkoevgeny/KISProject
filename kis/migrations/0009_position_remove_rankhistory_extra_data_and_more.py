# Generated by Django 5.0.4 on 2024-10-10 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kis', '0008_remove_cadet_school_average_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ('id',),
            },
        ),
        migrations.RemoveField(
            model_name='rankhistory',
            name='extra_data',
        ),
        migrations.AddField(
            model_name='encouragement',
            name='encouragement_order_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приказа'),
        ),
        migrations.AddField(
            model_name='encouragement',
            name='encouragement_order_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер приказа'),
        ),
        migrations.AddField(
            model_name='encouragement',
            name='encouragement_order_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.orderowner', verbose_name='Чей приказ'),
        ),
        migrations.AddField(
            model_name='rank',
            name='deadline',
            field=models.IntegerField(blank=True, null=True, verbose_name='Срок в месяцах до следующего звания'),
        ),
        migrations.AddField(
            model_name='rankhistory',
            name='rank_extra_data',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AddField(
            model_name='rankhistory',
            name='rank_order_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приказа'),
        ),
        migrations.AddField(
            model_name='rankhistory',
            name='rank_order_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер приказа'),
        ),
        migrations.AddField(
            model_name='rankhistory',
            name='rank_order_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.orderowner', verbose_name='Чей приказ'),
        ),
        migrations.AlterField(
            model_name='encouragement',
            name='encouragement_cadet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.cadet', verbose_name='На кого'),
        ),
        migrations.AlterField(
            model_name='encouragement',
            name='encouragement_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата поощрения'),
        ),
        migrations.AlterField(
            model_name='encouragement',
            name='encouragement_extra_data',
            field=models.TextField(blank=True, null=True, verbose_name='Фабула'),
        ),
        migrations.AlterField(
            model_name='encouragement',
            name='encouragement_kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.encouragementkind', verbose_name='Вид поощрения'),
        ),
        migrations.AlterField(
            model_name='encouragementkind',
            name='encouragement_kind',
            field=models.CharField(max_length=255, verbose_name='Вид поощрения'),
        ),
        migrations.AlterField(
            model_name='rankhistory',
            name='cadet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.cadet', verbose_name='Курсант'),
        ),
        migrations.AlterField(
            model_name='rankhistory',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.rank', verbose_name='Звание'),
        ),
        migrations.CreateModel(
            name='PositionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_date', models.DateField(blank=True, null=True, verbose_name='Дата назначения на должность')),
                ('position_order_date', models.DateField(blank=True, null=True, verbose_name='Дата приказа')),
                ('position_order_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер приказа')),
                ('position_extra_data', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('cadet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.cadet', verbose_name='Курсант')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.position', verbose_name='Должность')),
                ('position_order_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.orderowner', verbose_name='Чей приказ')),
            ],
            options={
                'verbose_name': 'Присвоение звания',
                'verbose_name_plural': 'Присвоение званий',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='SpecialityHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality_order_date', models.DateField(blank=True, null=True, verbose_name='Дата приказа')),
                ('speciality_order_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер приказа')),
                ('speciality_extra_data', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('cadet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.cadet', verbose_name='Курсант')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kis.speciality', verbose_name='Специальность')),
                ('speciality_order_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kis.orderowner', verbose_name='Чей приказ')),
            ],
            options={
                'verbose_name': 'Присвоение звания',
                'verbose_name_plural': 'Присвоение званий',
                'ordering': ('id',),
            },
        ),
    ]
