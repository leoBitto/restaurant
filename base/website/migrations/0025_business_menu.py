# Generated by Django 4.1.6 on 2023-02-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_opening_hour_weekdays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(auto_now=True)),
                ('dessert', models.ManyToManyField(blank=True, to='website.dessert')),
                ('entree', models.ManyToManyField(blank=True, to='website.entree')),
                ('first_dish', models.ManyToManyField(blank=True, to='website.first_dish')),
                ('second_dish', models.ManyToManyField(blank=True, to='website.second_dish')),
                ('side_dish', models.ManyToManyField(blank=True, to='website.side_dish')),
            ],
            options={
                'verbose_name_plural': 'Business_Menues',
                'ordering': ['-pub_date'],
            },
        ),
    ]
