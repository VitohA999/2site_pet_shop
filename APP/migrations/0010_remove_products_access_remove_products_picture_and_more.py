# Generated by Django 4.1.5 on 2023-03-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0009_remove_products_silka_products_access_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='access',
        ),
        migrations.RemoveField(
            model_name='products',
            name='picture',
        ),
        migrations.AddField(
            model_name='products',
            name='link',
            field=models.URLField(default=0, max_length=128),
        ),
    ]
