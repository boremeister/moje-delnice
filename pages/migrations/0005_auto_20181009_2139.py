# Generated by Django 2.1.1 on 2018-10-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_exchangerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='rate',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]