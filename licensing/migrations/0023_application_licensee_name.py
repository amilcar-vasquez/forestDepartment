# Generated by Django 4.1.9 on 2024-06-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0022_application_source_of_lumber_alter_lumber_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='licensee_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]