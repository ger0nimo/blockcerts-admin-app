# Generated by Django 2.1.3 on 2018-11-24 01:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0004_auto_20181124_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='add_issuer_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 1, 16, 53, 296171, tzinfo=utc)),
        ),
    ]