# Generated by Django 4.1.1 on 2022-09-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0003_remove_ingredient_grocery_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='grapes',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='wine',
            name='producer',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='wine',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='wine',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]