# Generated by Django 5.0.6 on 2024-07-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_type',
            name='title',
            field=models.CharField(default='Main Dishes', max_length=155, verbose_name='Заголовка'),
        ),
    ]
