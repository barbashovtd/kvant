# Generated by Django 3.2.4 on 2021-08-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial_squashed_0012_alter_student_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='Казань', max_length=32, unique=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.CharField(default='Татарстан', max_length=64, unique=True, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото (файл)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото (файл)'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото (файл)'),
        ),
    ]
