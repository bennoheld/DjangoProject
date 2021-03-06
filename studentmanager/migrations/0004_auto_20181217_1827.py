# Generated by Django 2.1.4 on 2018-12-17 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('studentmanager', '0003_auto_20181217_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='exam_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studentmanager.Exam',
                                    verbose_name='Prüfungsnummer'),
        ),
        migrations.AlterField(
            model_name='result',
            name='matriculation_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studentmanager.Student',
                                    verbose_name='Matrikelnummer'),
        ),
    ]
