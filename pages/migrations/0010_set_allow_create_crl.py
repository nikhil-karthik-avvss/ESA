# Generated by Django 3.2.18 on 2024-05-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20240515_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='Allow_Create_CRL',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
