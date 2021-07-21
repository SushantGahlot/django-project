# Generated by Django 3.2.5 on 2021-07-18 21:08

from django.db import migrations
from django.conf import settings
from sqlalchemy import create_engine
import pandas as pd
import os


def init_db(apps, schema_editor):
    Invoice = apps.get_model('invoice', 'Invoice')
    df = pd.read_parquet(
        os.getenv("PARQUET_FILE",
                  default=os.path.join(os.path.abspath(os.path.join(__file__, "../../..")), "test_invoices.parquet"))
    )

    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']
    host = settings.DATABASES['default']['HOST']

    database_url = 'postgresql://{user}:{password}@{host}:5432/{database_name}'.format(
        user=user,
        password=password,
        database_name=database_name,
        host=host,
    )

    engine = create_engine(database_url, echo=False)
    df.to_sql(Invoice._meta.db_table, con=engine,
              if_exists="append", index=False)


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_db)
    ]
