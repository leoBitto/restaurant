# Generated by Django 4.1.1 on 2022-09-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='gallery',
            name='header',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='gallery',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]