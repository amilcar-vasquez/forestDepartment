# Generated by Django 4.1.9 on 2024-04-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
        ('licensing', '0011_remove_lumber_application_remove_species_application_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='files',
            field=models.ManyToManyField(blank=True, to='files.file'),
        ),
    ]
