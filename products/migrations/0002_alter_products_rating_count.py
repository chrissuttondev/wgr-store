# Generated by Django 4.2 on 2024-05-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='rating_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
