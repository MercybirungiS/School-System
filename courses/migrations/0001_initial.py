# Generated by Django 3.2.6 on 2021-08-10 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=12, null=True)),
                ('course_code', models.CharField(blank=True, max_length=12, null=True)),
                ('trainer', models.CharField(blank=True, max_length=12, null=True)),
                ('course_description', models.CharField(blank=True, max_length=12, null=True)),
                ('stack', models.CharField(blank=True, max_length=12, null=True)),
                ('course_material', models.FileField(blank=True, null=True, upload_to='files/')),
                ('course_duration', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]
