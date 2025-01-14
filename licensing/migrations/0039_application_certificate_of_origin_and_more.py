# Generated by Django 4.1.9 on 2024-07-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0038_application_export_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='certificate_of_origin',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='application',
            name='export_permit',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='application',
            name='legal_acquisition',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d/'),
        ),
    ]
