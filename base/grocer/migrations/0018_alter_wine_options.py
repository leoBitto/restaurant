# Generated by Django 4.1.1 on 2022-10-09 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0017_remove_wine_cost_from_producer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wine',
            options={'ordering': ['order']},
        ),
    ]