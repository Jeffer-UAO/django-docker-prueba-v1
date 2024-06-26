# Generated by Django 4.0.2 on 2024-02-24 01:53

import core.security.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=13, unique=True, verbose_name='Número de cedula o ruc')),
                ('mobile', models.CharField(max_length=10, unique=True, verbose_name='Teléfono')),
                ('birthdate', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(max_length=500, verbose_name='Dirección')),
                ('identification_type', models.CharField(choices=[('05', 'CEDULA'), ('04', 'RUC'), ('06', 'PASAPORTE'), ('07', 'VENTA A CONSUMIDOR FINAL*'), ('08', 'IDENTIFICACION DELEXTERIOR*')], default='05', max_length=30, verbose_name='Tipo de identificación')),
                ('send_email_invoice', models.BooleanField(default=True, verbose_name='¿Enviar email de factura?')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='CreditNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('motive', models.CharField(blank=True, max_length=300, null=True, verbose_name='Motivo')),
                ('voucher_number', models.CharField(max_length=9, verbose_name='Número de comprobante')),
                ('voucher_number_full', models.CharField(max_length=20, verbose_name='Número de comprobante completo')),
                ('subtotal_12', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal 12%')),
                ('subtotal_0', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal 0%')),
                ('total_dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor del descuento')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Iva')),
                ('total_iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor de iva')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Total a pagar')),
                ('environment_type', models.PositiveIntegerField(choices=[(1, 'PRUEBAS'), (2, 'PRODUCCIÓN')], default=1)),
                ('access_code', models.CharField(blank=True, max_length=49, null=True, verbose_name='Clave de acceso')),
                ('authorization_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de autorización')),
                ('xml_authorized', core.security.fields.CustomFileField(blank=True, null=True, upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='XML Autorizado')),
                ('pdf_authorized', core.security.fields.CustomFileField(upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='PDF Autorizado')),
                ('create_electronic_invoice', models.BooleanField(default=True, verbose_name='Crear factura electrónica')),
                ('status', models.CharField(choices=[('without_authorizing', 'Sin Autorizar'), ('authorized', 'Autorizada'), ('authorized_and_sent_by_email', 'Autorizada y enviada por email'), ('canceled', 'Anulado')], default='without_authorizing', max_length=50, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Nota de Credito',
                'verbose_name_plural': 'Notas de Credito',
                'permissions': (('view_credit_note', 'Can view Nota de Credito'), ('add_credit_note', 'Can add Nota de Credito'), ('delete_credit_note', 'Can delete Nota de Credito'), ('view_credit_note_client', 'Can view_credit_note_client Nota de Credito')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='CreditNoteDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('cant', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('price_with_vat', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total_iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total_dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
            options={
                'verbose_name': 'Detalle Devolución Ventas',
                'verbose_name_plural': 'Detalle Devoluciones Ventas',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='CtasCollect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField(default=datetime.datetime.now)),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cuenta por cobrar',
                'verbose_name_plural': 'Cuentas por cobrar',
                'permissions': (('view_ctas_collect', 'Can view Cuenta por cobrar'), ('add_ctas_collect', 'Can add Cuenta por cobrar'), ('delete_ctas_collect', 'Can delete Cuenta por cobrar')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='DebtsPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField(default=datetime.datetime.now)),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cuenta por pagar',
                'verbose_name_plural': 'Cuentas por pagar',
                'permissions': (('view_debts_pay', 'Can view Cuenta por pagar'), ('add_debts_pay', 'Can add Cuenta por pagar'), ('delete_debts_pay', 'Can delete Cuenta por pagar')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Registro')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Gasto',
                'verbose_name_plural': 'Gastos',
            },
        ),
        migrations.CreateModel(
            name='PaymentsCtaCollect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Detalles')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Pago Cuenta por cobrar',
                'verbose_name_plural': 'Pagos Cuentas por cobrar',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PaymentsDebtsPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Detalles')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Det. Cuenta por pagar',
                'verbose_name_plural': 'Det. Cuentas por pagar',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Compra')),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Venta')),
                ('image', core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Imagen')),
                ('barcode', core.security.fields.CustomImageField(blank=True, null=True, upload_to=core.security.fields.CustomImageField.get_upload_path, verbose_name='Código de barra')),
                ('inventoried', models.BooleanField(default=True, verbose_name='¿Es inventariado?')),
                ('stock', models.IntegerField(default=0)),
                ('with_tax', models.BooleanField(default=True, verbose_name='¿Se cobra impuesto?')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'permissions': (('view_product', 'Can view Producto'), ('add_product', 'Can add Producto'), ('change_product', 'Can change Producto'), ('delete_product', 'Can delete Producto'), ('adjust_product_stock', 'Can adjust_product_stock Producto')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('end_date', models.DateField(default=datetime.datetime.now)),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Promoción',
                'verbose_name_plural': 'Promociones',
            },
        ),
        migrations.CreateModel(
            name='PromotionsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_current', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total_dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('price_final', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
            options={
                'verbose_name': 'Detalle Promoción',
                'verbose_name_plural': 'Detalle de Promociones',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Razón Social')),
                ('ruc', models.CharField(max_length=13, unique=True, verbose_name='Número de RUC')),
                ('mobile', models.CharField(max_length=10, unique=True, verbose_name='Teléfono celular')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=8, unique=True, verbose_name='Número de factura')),
                ('payment_type', models.CharField(choices=[('efectivo', 'Efectivo'), ('credito', 'Credito')], default='efectivo', max_length=50, verbose_name='Tipo de pago')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('end_credit', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de plazo de credito')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'permissions': (('view_purchase', 'Can view Compra'), ('add_purchase', 'Can add Compra'), ('delete_purchase', 'Can delete Compra')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
            options={
                'verbose_name': 'Detalle de Compra',
                'verbose_name_plural': 'Detalle de Compras',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('start_number', models.PositiveIntegerField(default=1, verbose_name='Desde')),
                ('end_number', models.PositiveIntegerField(default=999999999, verbose_name='Hasta')),
                ('current_number', models.PositiveIntegerField(default=999999999, verbose_name='Actual')),
            ],
            options={
                'verbose_name': 'Comprobante',
                'verbose_name_plural': 'Comprobantes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_number', models.CharField(max_length=9, verbose_name='Número de comprobante')),
                ('voucher_number_full', models.CharField(max_length=20, verbose_name='Número de comprobante completo')),
                ('payment_type', models.CharField(choices=[('efectivo', 'Efectivo'), ('credito', 'Credito')], default='efectivo', max_length=50, verbose_name='Tipo de pago')),
                ('payment_method', models.CharField(choices=[('01', 'SIN UTILIZACION DEL SISTEMA FINANCIERO'), ('15', 'COMPENSACIÓN DE DEUDAS'), ('16', 'TARJETA DE DÉBITO'), ('17', 'DINERO ELECTRÓNICO'), ('18', 'TARJETA PREPAGO'), ('20', 'OTROS CON UTILIZACION DEL SISTEMA FINANCIERO'), ('21', 'ENDOSO DE TÍTULOS')], default='20', max_length=50, verbose_name='Método de pago')),
                ('time_limit', models.IntegerField(default=31, verbose_name='Plazo')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha y hora de registro')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('end_credit', models.DateField(default=datetime.datetime.now, verbose_name='Fecha limite de credito')),
                ('additional_info', models.JSONField(default=dict, verbose_name='Información adicional')),
                ('subtotal_12', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal 12%')),
                ('subtotal_0', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal 0%')),
                ('total_dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor del descuento')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Iva')),
                ('total_iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor de iva')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Total a pagar')),
                ('cash', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Efectivo recibido')),
                ('change', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Cambio')),
                ('environment_type', models.PositiveIntegerField(choices=[(1, 'PRUEBAS'), (2, 'PRODUCCIÓN')], default=1)),
                ('access_code', models.CharField(blank=True, max_length=49, null=True, verbose_name='Clave de acceso')),
                ('authorization_date', models.DateField(blank=True, null=True, verbose_name='Fecha de emisión')),
                ('xml_authorized', core.security.fields.CustomFileField(blank=True, null=True, upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='XML Autorizado')),
                ('pdf_authorized', core.security.fields.CustomFileField(blank=True, null=True, upload_to=core.security.fields.CustomFileField.get_upload_path, verbose_name='PDF Autorizado')),
                ('create_electronic_invoice', models.BooleanField(default=True, verbose_name='Crear factura electrónica')),
                ('status', models.CharField(choices=[('without_authorizing', 'Sin Autorizar'), ('authorized', 'Autorizada'), ('authorized_and_sent_by_email', 'Autorizada y enviada por email'), ('canceled', 'Anulado')], default='without_authorizing', max_length=50, verbose_name='Estado')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pos.client', verbose_name='Cliente')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.company', verbose_name='Compañia')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'permissions': (('view_sale', 'Can view Venta'), ('add_sale', 'Can add Venta'), ('delete_sale', 'Can delete Venta'), ('view_sale_client', 'Can view_sale_client Venta')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TypeExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de Gasto',
                'verbose_name_plural': 'Tipos de Gastos',
                'permissions': (('view_type_expense', 'Can view Tipo de Gasto'), ('add_type_expense', 'Can add Tipo de Gasto'), ('change_type_expense', 'Can change Tipo de Gasto'), ('delete_type_expense', 'Can delete Tipo de Gasto')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='VoucherErrors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('datetime_joined', models.DateTimeField(default=datetime.datetime.now)),
                ('environment_type', models.PositiveIntegerField(choices=[(1, 'PRUEBAS'), (2, 'PRODUCCIÓN')], default=1)),
                ('reference', models.CharField(max_length=20)),
                ('stage', models.CharField(choices=[('xml_creation', 'Creación del XML'), ('xml_signature', 'Firma del XML'), ('xml_validation', 'Validación del XML'), ('xml_authorized', 'Autorización del XML'), ('sent_by_email', 'Enviado por email')], default='xml_creation', max_length=20)),
                ('errors', models.JSONField(default=dict)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.receipt')),
            ],
            options={
                'verbose_name': 'Errores del Comprobante',
                'verbose_name_plural': 'Errores de los Comprobantes',
                'permissions': (('view_voucher_errors', 'Can view Errores del Comprobante'), ('delete_voucher_errors', 'Can delete Errores del Comprobante')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('price_with_vat', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total_iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total_dscto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pos.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.sale')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalle de Ventas',
                'default_permissions': (),
            },
        ),
    ]
