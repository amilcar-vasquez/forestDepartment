# Generated by Django 4.1.9 on 2024-06-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0024_application_sawmill_address_application_sawmill_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='license_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
