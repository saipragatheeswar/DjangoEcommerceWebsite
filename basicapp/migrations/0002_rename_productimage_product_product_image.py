# Generated by Django 3.2.25 on 2024-06-20 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productimage',
            new_name='product_image',
        ),
    ]
