# Generated by Django 3.0.3 on 2020-03-09 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0008_auto_20200309_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='loan',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 9, 13, 40, 32, 334642, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 23, 13, 40, 32, 334642, tzinfo=utc)),
        ),
    ]
