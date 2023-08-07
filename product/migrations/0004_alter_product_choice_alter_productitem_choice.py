# Generated by Django 4.2.3 on 2023-07-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='choice',
            field=models.CharField(choices=[(1, 'SUM'), (2, '$')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='choice',
            field=models.CharField(choices=[(1, 'KG'), (2, 'COUNT')], default=1, max_length=10),
        ),
    ]
