# Generated by Django 3.2.25 on 2024-07-23 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240723_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app.category'),
        ),
    ]
