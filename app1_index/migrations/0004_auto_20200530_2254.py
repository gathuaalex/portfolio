# Generated by Django 3.0.6 on 2020-05-30 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_index', '0003_interests_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='interests',
            name='interst_title',
            field=models.CharField(default='SWIMMING', max_length=11),
        ),
        migrations.AddField(
            model_name='lang',
            name='language_status',
            field=models.CharField(default='FLUENT', max_length=6),
        ),
        migrations.AddField(
            model_name='lang',
            name='language_title',
            field=models.CharField(default='ENGLISH', max_length=11),
        ),
    ]