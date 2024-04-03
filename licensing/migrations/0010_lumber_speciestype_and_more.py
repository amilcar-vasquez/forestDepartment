# Generated by Django 4.1.9 on 2024-04-03 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licensing', '0009_alter_profile_photo_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('grade', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpeciesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Live Specimen', 'Live Specimen'), ('Plant Sample', 'Plant Sample'), ('Blood Sample', 'Blood Sample'), ('Tissue Sample', 'Tissue Sample'), ('Feather Sample', 'Feather Sample'), ('Swab Sample', 'Swab Sample (Buccal/Skin)'), ('Other', 'Other')], max_length=100)),
                ('number_of_individuals', models.IntegerField(default=1)),
                ('mode_of_storage', models.CharField(blank=True, max_length=100, null=True)),
                ('tests_to_be_conducted', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='species',
            old_name='application',
            new_name='Application',
        ),
        migrations.RenameField(
            model_name='species',
            old_name='quantity',
            new_name='number_of_individuals',
        ),
        migrations.RemoveField(
            model_name='application',
            name='description_of_goods',
        ),
        migrations.RemoveField(
            model_name='species',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='species',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='species',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='species',
            name='scientific_name',
        ),
        migrations.RemoveField(
            model_name='species',
            name='value',
        ),
        migrations.AddField(
            model_name='species',
            name='CITES_status',
            field=models.CharField(choices=[('Appendix I', 'Appendix I'), ('Appendix II', 'Appendix II'), ('Appendix III', 'Appendix III'), ('Not Listed', 'Not Listed')], default='Not Listed', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='species',
            name='class_of_goods',
            field=models.CharField(choices=[('Research', 'Research'), ('Pet', 'Pet'), ('Other', 'Other')], default='Other', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='species',
            name='country_of_origin',
            field=models.CharField(default='Belize', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='species',
            name='identification',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='species',
            name='name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.AddField(
            model_name='speciestype',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='licensing.species'),
        ),
        migrations.AddField(
            model_name='lumber',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='licensing.application'),
        ),
    ]
