from django.db import models

REGEX_WORD_PATTERN = r'\W+'

REPORTED_STATUS = {
    'reported': 2,
    'not reported': 0,
    'rejected': -1
}


class TransactionType(models.TextChoices):
    PURCHASE = 'purchase', 'PURCHASE'
    SALE = 'sale', 'SALE'


class StatusStart(models.TextChoices):
    CANCELLED = 'CANCELLED', 'CANCELLED'
    DRAFT = 'DRAFT', 'DRAFT'
    REQUIRE_ACTION = 'REQUIRE_ACTION', 'REQUIRE_ACTION'


class StatusTaxSummary(models.TextChoices):
    APPROVED = 'APPROVED', 'APPROVED'
    DRAFT = 'DRAFT', 'DRAFT'
    IN_PROGRESS = 'IN_PROGRESS', 'IN_PROGRESS'
    NONE = None, 'None'
    REJECTED = 'REJECTED', 'REJECTED'


class ReportedStatusDescription(models.TextChoices):
    NONE = None, 'None'
    REPORTED = 'reported', 'reported'
    NOT_REPORTED = 'not reported', 'not reported'
    REJECTED = 'rejected', 'rejected'


class TaxType(models.TextChoices):
    NONE = None, 'None'
    PPHFINAL = 'pphFinal', 'pphFinal'
    PPN = 'ppn', 'ppn'
