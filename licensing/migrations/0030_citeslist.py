# Generated by Django 4.1.9 on 2024-06-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0029_delete_speciestype'),
    ]

    operations = [
        migrations.CreateModel(
            name='CITESList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CITES_id', models.CharField(max_length=100)),
                ('kingdom', models.CharField(blank=True, max_length=100, null=True)),
                ('phylum', models.CharField(blank=True, max_length=100, null=True)),
                ('class_name', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.CharField(blank=True, max_length=100, null=True)),
                ('family', models.CharField(blank=True, max_length=100, null=True)),
                ('genus', models.CharField(blank=True, max_length=100, null=True)),
                ('species', models.CharField(max_length=100)),
                ('sub_species', models.CharField(blank=True, max_length=100, null=True)),
                ('scientific_name', models.CharField(max_length=100)),
                ('rank', models.CharField(blank=True, max_length=100, null=True)),
                ('listing', models.CharField(choices=[('I', 'Appendix I'), ('II', 'Appendix II'), ('III', 'Appendix III')], max_length=100)),
            ],
        ),
    ]
