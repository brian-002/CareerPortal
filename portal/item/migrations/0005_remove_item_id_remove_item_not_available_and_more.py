# Generated by Django 4.2.2 on 2023-06-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_category_alter_item_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='not_available',
        ),
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='position',
            field=models.CharField(max_length=255, primary_key='Position', serialize=False),
        ),
    ]
