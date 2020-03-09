# Generated by Django 3.0.3 on 2020-03-09 00:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_auto_20200306_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.Book'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='checkout_date',
            field=models.DateField(default=datetime.date(2020, 3, 9)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='library_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.LibraryUser'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateField(default=datetime.date(2020, 3, 23)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
