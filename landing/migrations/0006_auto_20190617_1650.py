# Generated by Django 2.2.2 on 2019-06-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20190617_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Availability',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]