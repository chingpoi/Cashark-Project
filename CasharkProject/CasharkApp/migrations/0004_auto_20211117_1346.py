# Generated by Django 3.2.6 on 2021-11-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CasharkApp', '0003_auto_20211116_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Credit_Score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
