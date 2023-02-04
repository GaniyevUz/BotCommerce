# Generated by Django 4.1.6 on 2023-02-04 10:50

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.JSONField(default=products.models.Category.Translate.default_translate)),
                ('description', models.JSONField(default=products.models.Category.Translate.default_translate)),
                ('emoji', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop/categories/')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/%m')),
                ('price', models.IntegerField()),
                ('in_availability', models.BooleanField(default=True)),
                ('length', models.CharField(blank=True, max_length=50, null=True)),
                ('width', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('length_class', models.CharField(blank=True, choices=[('m', 'Metre'), ('cm', 'CM')], max_length=10, null=True)),
                ('weight_class', models.CharField(blank=True, choices=[('kg', 'KG'), ('gram', 'Gram')], max_length=10, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
