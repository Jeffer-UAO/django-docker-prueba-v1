# Generated by Django 4.0.2 on 2024-03-19 11:00

import core.security.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_alter_category_image_alter_creditnote_pdf_authorized_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='pdf_authorized',
            field=core.security.fields.CustomFileField(upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='PDF Autorizado'),
        ),
        migrations.AlterField(
            model_name='creditnote',
            name='xml_authorized',
            field=core.security.fields.CustomFileField(blank=True, null=True, upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='XML Autorizado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Código de barra'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='ruc',
            field=models.CharField(max_length=13, unique=True, verbose_name='Número de NIT'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='pdf_authorized',
            field=core.security.fields.CustomFileField(blank=True, null=True, upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='PDF Autorizado'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='xml_authorized',
            field=core.security.fields.CustomFileField(blank=True, null=True, upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='XML Autorizado'),
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.sale')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalle de Ventas',
                'ordering': ['id'],
                'default_permissions': (),
            },
        ),
    ]
