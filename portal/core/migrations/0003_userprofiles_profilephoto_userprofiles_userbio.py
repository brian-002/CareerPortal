# Generated by Django 4.2.2 on 2023-07-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofiles_sname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='profilephoto',
            field=models.ImageField(null=True, upload_to='account_photos', verbose_name='profile photo'),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='userbio',
            field=models.TextField(null=True),
        ),
    ]
