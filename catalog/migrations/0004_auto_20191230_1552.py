# Generated by Django 3.0.1 on 2019-12-30 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191230_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]