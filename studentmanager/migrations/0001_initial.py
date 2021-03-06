# Generated by Django 2.1.4 on 2018-12-12 17:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(6),
                                                                        django.core.validators.MinValueValidator(1)])),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studentmanager.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('matriculation_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='matriculation_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studentmanager.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('matriculation_number', 'exam_id')},
        ),
    ]
