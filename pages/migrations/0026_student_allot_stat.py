# Generated by Django 3.2.18 on 2024-06-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_auto_20240616_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Allot_Stat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
