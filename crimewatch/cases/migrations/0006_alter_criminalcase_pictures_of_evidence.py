# Generated by Django 5.0 on 2024-06-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_remove_criminalcase_associated_case_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminalcase',
            name='pictures_of_evidence',
            field=models.ImageField(blank=True, null=True, upload_to='src/images/'),
        ),
    ]
