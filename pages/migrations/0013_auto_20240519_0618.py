# Generated by Django 3.2.18 on 2024-05-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20240516_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicelisttable',
            name='College_ID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choicelisttable',
            name='College',
            field=models.CharField(max_length=100),
        ),
    ]
