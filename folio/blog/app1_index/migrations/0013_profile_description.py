# Generated by Django 3.0.6 on 2020-06-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_index', '0012_auto_20200623_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]