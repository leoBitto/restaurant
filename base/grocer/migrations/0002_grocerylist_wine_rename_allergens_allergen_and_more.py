# Generated by Django 4.1.1 on 2022-09-23 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Allergens',
            new_name='Allergen',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='grocery_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='grocer.grocerylist'),
        ),
    ]