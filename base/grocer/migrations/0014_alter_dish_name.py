# Generated by Django 4.1.1 on 2022-10-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0013_remove_dish_ingredients_menu_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(blank=True, default='Menu', max_length=300, null=True),
        ),
    ]