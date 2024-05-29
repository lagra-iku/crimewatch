# Generated by Django 5.0 on 2024-05-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0003_criminalrecord_crime_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminalrecord',
            old_name='crime_type',
            new_name='crime_committed',
        ),
        migrations.AddField(
            model_name='criminalrecord',
            name='is_incarcerated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='criminalrecord',
            name='is_wanted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='contact_info',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='known_aliases',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='next_of_kin',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='criminalrecord',
            name='religion',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]