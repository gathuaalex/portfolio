# Generated by Django 2.2.8 on 2020-09-10 19:08

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1_index', '0012_auto_20200623_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myimage', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='prof_image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1_index.ProfileImage'),
        ),
    ]
