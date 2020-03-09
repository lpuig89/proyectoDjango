# Generated by Django 3.0.3 on 2020-03-09 16:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0012_auto_20200309_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Book'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 9, 16, 38, 34, 862931, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 23, 16, 38, 34, 862931, tzinfo=utc)),
        ),
    ]
