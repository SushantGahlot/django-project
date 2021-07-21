# Generated by Django 3.2.5 on 2021-07-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField()),
                ('company_id', models.UUIDField()),
                ('company_name', models.CharField(max_length=255)),
                ('npwp', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
                ('invoice_id', models.UUIDField()),
                ('vendor_id', models.UUIDField()),
                ('vendor_name', models.CharField(max_length=255)),
                ('transaction_type', models.CharField(choices=[('purchase', 'PURCHASE'), ('sale', 'SALE')], max_length=8)),
                ('commercial_invoice_number', models.BigIntegerField()),
                ('status_start', models.CharField(choices=[('CANCELLED', 'CANCELLED'), ('DRAFT', 'DRAFT'), ('REQUIRE_ACTION', 'REQUIRE_ACTION')], max_length=14)),
                ('status_tax_summary', models.CharField(choices=[('APPROVED', 'APPROVED'), ('DRAFT', 'DRAFT'), ('IN_PROGRESS', 'IN_PROGRESS'), ('None', 'None'), ('REJECTED', 'REJECTED')], max_length=11, null=True)),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField()),
                ('item_name', models.CharField(max_length=255)),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('discount', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('gross_amount', models.DecimalField(decimal_places=1, max_digits=15, null=True)),
                ('tax_amount', models.DecimalField(decimal_places=1, max_digits=15, null=True)),
                ('total_amount', models.DecimalField(decimal_places=10, max_digits=30, null=True)),
                ('tax_period', models.CharField(max_length=255, null=True)),
                ('revision', models.IntegerField(null=True)),
                ('reported_date', models.DateField(null=True)),
                ('reported_status', models.IntegerField(null=True)),
                ('reported_status_desc', models.CharField(choices=[('None', 'None'), ('reported', 'reported'), ('not reported', 'not reported'), ('rejected', 'rejected')], max_length=12, null=True)),
                ('tax_type', models.CharField(choices=[('None', 'None'), ('pphFinal', 'pphFinal'), ('ppn', 'ppn')], max_length=8, null=True)),
                ('tax_document_number', models.CharField(max_length=255)),
                ('tax_document_date', models.DateField(null=True)),
                ('approved_date', models.DateField(null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='invoice',
            index=models.Index(fields=['company_name'], name='invoice_inv_company_64a8d8_idx'),
        ),
    ]