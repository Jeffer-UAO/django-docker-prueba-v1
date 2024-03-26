# Generated by Django 4.0.2 on 2024-03-08 08:09

import core.security.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0034_alter_dashboard_image_alter_databasebackups_archive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='image',
            field=core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='databasebackups',
            name='archive',
            field=core.security.fields.CustomFileField(upload_to=core.security.fields.CustomFileField.get_upload_path),
        ),
        migrations.AlterField(
            model_name='module',
            name='image',
            field=core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Imagen'),
        ),
    ]
