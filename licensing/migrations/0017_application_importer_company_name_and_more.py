# Generated by Django 4.1.9 on 2024-05-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0016_application_goods_alter_application_approval_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='importer_company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='type',
            field=models.CharField(choices=[('Import', 'Import'), ('Export', 'Export'), ('Re-export', 'Re-export')], max_length=100),
        ),
    ]