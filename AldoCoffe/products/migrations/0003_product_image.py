# Generated by Django 5.0.6 on 2024-05-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='product/'),
            preserve_default=False,
        ),
    ]
