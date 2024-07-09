# Generated by Django 4.1.9 on 2024-06-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0031_citeslist_common_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='port_of_entry',
            new_name='port_of_entry_bz',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='port_of_exit',
            new_name='port_of_exit_bz',
        ),
        migrations.AddField(
            model_name='application',
            name='port_of_entry_int',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='port_of_exit_int',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]