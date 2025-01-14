# Generated by Django 4.1.9 on 2024-06-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0027_lumber_cubic_meters_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='species',
            old_name='name',
            new_name='local_name',
        ),
        migrations.AddField(
            model_name='species',
            name='scientific_name',
            field=models.CharField(default='default_scientific_name', max_length=100),
            preserve_default=False,
        ),
    ]
