# Generated by Django 3.2.4 on 2021-08-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='inst',
            field=models.CharField(blank=True, max_length=31, verbose_name='Инстаграм'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='tg',
            field=models.CharField(blank=True, max_length=33, verbose_name='Телеграм'),
        ),
        migrations.AlterField(
            model_name='student',
            name='inst',
            field=models.CharField(blank=True, max_length=31, verbose_name='Инстаграм'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tg',
            field=models.CharField(blank=True, max_length=33, verbose_name='Телеграм'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='inst',
            field=models.CharField(blank=True, max_length=31, verbose_name='Инстаграм'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tg',
            field=models.CharField(blank=True, max_length=33, verbose_name='Телеграм'),
        ),
    ]
