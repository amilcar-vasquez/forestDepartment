# Generated by Django 4.1.9 on 2024-03-15 03:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0004_alter_application_description_of_goods_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='approval',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Conditional', 'Approved with Conditions'), ('Not Approved', 'Not Approved')], default='Not Approved', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='date_received',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
