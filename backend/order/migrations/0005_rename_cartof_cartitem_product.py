# Generated by Django 4.0.3 on 2022-04-03 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_product_cartitem_cartof'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='cartOf',
            new_name='product',
        ),
    ]