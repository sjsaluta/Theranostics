# Generated by Django 4.2.3 on 2023-08-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0010_remove_physicalexam_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]