# Generated by Django 4.1.1 on 2022-09-30 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0005_wine_month_wine_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='month',
        ),
    ]