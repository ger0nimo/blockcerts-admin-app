# Generated by Django 2.2.5 on 2019-09-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0014_auto_20190920_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuance',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
