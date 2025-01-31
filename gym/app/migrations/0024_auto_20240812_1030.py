# Generated by Django 3.2.25 on 2024-08-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='cart/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='product/'),
        ),
    ]
