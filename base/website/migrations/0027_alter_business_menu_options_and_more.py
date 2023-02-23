# Generated by Django 4.1.6 on 2023-02-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_menu_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business_menu',
            options={'verbose_name_plural': 'Business_Menues'},
        ),
        migrations.RemoveField(
            model_name='business_menu',
            name='dessert',
        ),
        migrations.RemoveField(
            model_name='business_menu',
            name='entree',
        ),
        migrations.RemoveField(
            model_name='business_menu',
            name='first_dish',
        ),
        migrations.RemoveField(
            model_name='business_menu',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='business_menu',
            name='second_dish',
        ),
        migrations.RemoveField(
            model_name='business_menu',
            name='side_dish',
        ),
        migrations.AddField(
            model_name='business_menu',
            name='opzione1',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='business_menu',
            name='opzione2',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
