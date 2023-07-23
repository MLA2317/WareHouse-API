# Generated by Django 4.2.3 on 2023-07-20 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('cat_img', models.ImageField(null=True, upload_to='category/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_cat', to='category.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.IntegerField(choices=[(1, 'ZONA 1'), (2, 'ZONA 2'), (3, 'ZONA 3'), (4, 'ZONA 4'), (5, 'ZONA 5')], default=False)),
                ('product', models.CharField(max_length=221)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zona_cat', to='category.category')),
            ],
        ),
    ]
