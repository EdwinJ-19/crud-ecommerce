# Generated by Django 4.2.10 on 2024-03-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='cart_images',
            field=models.ImageField(upload_to='cart_images/'),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='cart_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='cart_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]