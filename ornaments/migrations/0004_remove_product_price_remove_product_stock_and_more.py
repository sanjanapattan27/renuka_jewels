# Generated by Django 5.0.6 on 2024-06-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ornaments', '0003_category_order_product_delete_user_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
