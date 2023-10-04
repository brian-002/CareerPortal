# Generated by Django 4.2.2 on 2023-07-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userprofiles_profilephoto_userprofiles_userbio'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='applicatindate',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='applicationletter',
            field=models.FileField(null=True, upload_to='documents', verbose_name='application letter'),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='nationalid',
            field=models.FileField(null=True, upload_to='documents', verbose_name='national id'),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='usercertificates',
            field=models.FileField(null=True, upload_to='documents', verbose_name='certificates'),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='usercv',
            field=models.FileField(null=True, upload_to='documents', verbose_name='curriculum vitae'),
        ),
    ]