# Generated by Django 4.2.4 on 2023-08-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_products_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]