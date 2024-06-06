# Generated by Django 4.1.9 on 2024-06-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0023_application_licensee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='sawmill_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sawmill_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='validity_period',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
