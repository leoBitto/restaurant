# Generated by Django 4.1.6 on 2023-02-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_rename_in_our_cellar_wine_bottles_in_our_cellar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
