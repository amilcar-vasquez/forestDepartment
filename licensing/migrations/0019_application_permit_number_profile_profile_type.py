# Generated by Django 4.1.9 on 2024-05-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0018_application_company_registry_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='permit_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Business', 'Business')], default='Individual', max_length=100),
            preserve_default=False,
        ),
    ]
