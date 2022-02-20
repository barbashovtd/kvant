# Generated by Django 3.2.4 on 2021-08-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210828_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='children',
            field=models.ManyToManyField(blank=True, to='core.Student', verbose_name='Дети'),
        ),
        migrations.AlterField(
            model_name='section',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='section_teachers', to='core.Teacher', verbose_name='Преподаватели'),
        ),
        migrations.AlterField(
            model_name='student',
            name='father',
            field=models.ManyToManyField(blank=True, related_name='student_father', to='core.Parent', verbose_name='Отец'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother',
            field=models.ManyToManyField(blank=True, related_name='student_mother', to='core.Parent', verbose_name='Мать'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='section',
            field=models.ManyToManyField(blank=True, related_name='teacher_sections', to='core.Section', verbose_name='Секция'),
        ),
    ]
