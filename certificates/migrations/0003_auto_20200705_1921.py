# Generated by Django 3.0.7 on 2020-07-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_auto_20200705_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
