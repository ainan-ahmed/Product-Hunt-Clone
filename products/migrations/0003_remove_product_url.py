# Generated by Django 2.2.10 on 2020-03-25 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200325_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
    ]
