# Generated by Django 2.1.7 on 2019-03-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_auto_20190323_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
