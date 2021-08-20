# Generated by Django 3.2.6 on 2021-08-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='stack',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='trainer',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]