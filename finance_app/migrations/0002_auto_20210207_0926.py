# Generated by Django 3.1.2 on 2021-02-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_id',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]