# Generated by Django 4.1.1 on 2022-09-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_dish_allergens_dish_allergen_celery_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='gallery_image',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='gallery_image',
            name='header',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
