# Generated by Django 4.2.3 on 2023-08-08 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Cancel', 'Cancelled'), ('Process', 'Process'), ('Shipped', 'Shipped')], max_length=7)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=16, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254)),
                ('enter_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.location')),
                ('products', models.ManyToManyField(related_name='warehouse_prod', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order_id', models.ManyToManyField(related_name='order_prod', to='warehouse.order')),
                ('products', models.ManyToManyField(related_name='order', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='warehouse_id',
            field=models.ManyToManyField(related_name='order_warehouse', to='warehouse.warehouse'),
        ),
        migrations.CreateModel(
            name='Leaving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_out', models.DateTimeField(auto_now_add=True)),
                ('order_prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.orderproduct')),
            ],
        ),
    ]
