# Generated by Django 3.2.4 on 2021-08-29 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210829_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.section', verbose_name='Секция'),
        ),
    ]
