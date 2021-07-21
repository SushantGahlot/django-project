from django.db import models
from .const import ReportedStatusDescription, TransactionType, StatusStart, StatusTaxSummary, TaxType, REPORTED_STATUS
from .cache_helper import get_cache_frequency, delete_cache_frequency


class Invoice(models.Model):
    user_id = models.UUIDField()
    company_id = models.UUIDField()
    company_name = models.CharField(max_length=255)
    npwp = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    post_code = models.IntegerField()
    invoice_id = models.UUIDField()
    vendor_id = models.UUIDField()
    vendor_name = models.CharField(max_length=255)
    transaction_type = models.CharField(
        choices=TransactionType.choices, max_length=8)
    commercial_invoice_number = models.BigIntegerField()
    status_start = models.CharField(choices=StatusStart.choices, max_length=14)
    status_tax_summary = models.CharField(
        choices=StatusTaxSummary.choices, max_length=11, null=True)
    invoice_date = models.DateField()
    due_date = models.DateField()
    item_name = models.CharField(max_length=255)
    unitprice = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    gross_amount = models.DecimalField(
        max_digits=15, decimal_places=1, null=True)
    tax_amount = models.DecimalField(
        max_digits=15, decimal_places=1, null=True)
    total_amount = models.DecimalField(
        max_digits=30, decimal_places=10, null=True)
    tax_period = models.CharField(max_length=255, null=True)
    revision = models.IntegerField(null=True)
    reported_date = models.DateField(null=True)
    reported_status = models.IntegerField(null=True)
    reported_status_desc = models.CharField(
        choices=ReportedStatusDescription.choices, max_length=12, null=True)
    tax_type = models.CharField(
        choices=TaxType.choices, max_length=8, null=True)
    tax_document_number = models.CharField(max_length=255)
    tax_document_date = models.DateField(null=True)
    approved_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        # Set reported status from reported status description
        self.reported_status = REPORTED_STATUS.get(self.reported_status_desc)

        # Check if cache key exists
        if get_cache_frequency(self.company_name, self.vendor_name) is not None:
            # Delete if the key exists
            delete_cache_frequency(self.company_name, self.vendor_name)
        super(Invoice, self).save(*args, **kwargs)

    class Meta:
        indexes = [models.Index(fields=['company_name', ]), ]
