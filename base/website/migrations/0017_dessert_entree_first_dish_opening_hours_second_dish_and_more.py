# Generated by Django 4.1.6 on 2023-02-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_rename_in_cellar_wine_in_our_cellar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='First_dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'First_dishes',
            },
        ),
        migrations.CreateModel(
            name='Opening_hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Second_dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Second_dishes',
            },
        ),
        migrations.CreateModel(
            name='Side_dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Side_dishes',
            },
        ),
        migrations.RenameField(
            model_name='wine',
            old_name='price',
            new_name='price_to_public',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='dishes',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='is_lunch',
        ),
        migrations.AddField(
            model_name='wine',
            name='price_from_vendor',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.AddField(
            model_name='menu',
            name='dessert',
            field=models.ManyToManyField(to='website.dessert'),
        ),
        migrations.AddField(
            model_name='menu',
            name='entree',
            field=models.ManyToManyField(to='website.entree'),
        ),
        migrations.AddField(
            model_name='menu',
            name='first_dish',
            field=models.ManyToManyField(to='website.first_dish'),
        ),
        migrations.AddField(
            model_name='menu',
            name='second_dish',
            field=models.ManyToManyField(to='website.second_dish'),
        ),
        migrations.AddField(
            model_name='menu',
            name='side_dish',
            field=models.ManyToManyField(to='website.side_dish'),
        ),
    ]