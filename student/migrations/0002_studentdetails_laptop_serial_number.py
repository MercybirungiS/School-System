# Generated by Django 3.2.6 on 2021-08-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='laptop_serial_number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]