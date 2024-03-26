# Generated by Django 4.0.2 on 2024-02-29 14:52

import core.security.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0003_alter_company_electronic_signature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='electronic_signature',
            field=core.security.fields.CustomFileField(blank=True, null=True, upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='Firma electrónica (Archivo P12)'),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Logotipo de la empresa'),
        ),
    ]
