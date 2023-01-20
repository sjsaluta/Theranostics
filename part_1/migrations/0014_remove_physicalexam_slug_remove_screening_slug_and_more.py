# Generated by Django 4.0.4 on 2023-01-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0013_rename_patient_name_physicalexam_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='physicalexam',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='slug',
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='bp',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]