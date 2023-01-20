# Generated by Django 4.0.4 on 2023-01-20 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0009_rename_gapsma_screening_gapsma_choices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Bone Lesion Status'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Bone Lesion Location'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bone Lesion Size'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_bone_suv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Bone SUV'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Brain Lesion Status'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Brain Lesion Location'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Brain Lesion Size'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_brain_suv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Brain SUV'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Liver Lesion Status'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Liver Lesion Location'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Liver Lesion Size'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_liver_suv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Liver SUV'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Lung Lesion Status'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Lung Lesion Location'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Lung Lesion Size'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lung_suv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Lung SUV'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Lymph Node Lesion Status'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Lymph Node Location'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Lymph Node Lesion Size'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_lymph_node_suv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Lymph Node SUV'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_lesion_status',
            field=models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Prostate Lesion Status'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Prostate Location'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Prostate Lesion Size'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_prostate_suv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Prostate SUV'),
        ),
    ]