# Generated by Django 5.0.6 on 2024-07-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_menu_menu_type_delete_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_type',
            name='title',
            field=models.CharField(choices=[('MAIN DISHES', 'MAIN DISHES'), ('DESSERTS', 'DESSERTS'), ('SEA FOOD', 'SEA FOOD'), ('BEVERAGE', ' BEVERAGE')], max_length=100),
        ),
    ]
