# Generated by Django 3.1.2 on 2021-02-08 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0005_auto_20210207_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='account_id',
            new_name='account',
        ),
    ]