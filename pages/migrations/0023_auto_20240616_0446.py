# Generated by Django 3.2.18 on 2024-06-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_image_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='Bus_Fee',
            field=models.IntegerField(default=60000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='College_Image',
            field=models.ImageField(default=0, upload_to='media/photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='Hostel_Fee_max',
            field=models.IntegerField(default=240000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='Hostel_Fee_min',
            field=models.IntegerField(default=102500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='Mand_Bus',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='Mess_Inc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='Tution_Fee',
            field=models.IntegerField(default=125000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='Web',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
