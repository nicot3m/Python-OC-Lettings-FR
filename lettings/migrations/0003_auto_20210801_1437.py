# Generated by Django 3.2 on 2021-08-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20210731_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='letting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
