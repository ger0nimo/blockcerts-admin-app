# Generated by Django 2.1.3 on 2019-03-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0011_auto_20190314_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='personissuances',
            name='unsigned_certificate',
            field=models.TextField(default=''),
        ),
    ]
