# Generated by Django 4.0.4 on 2023-01-20 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0014_remove_physicalexam_slug_remove_screening_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient_code',
        ),
    ]