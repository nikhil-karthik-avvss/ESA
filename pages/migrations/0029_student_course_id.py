# Generated by Django 3.2.18 on 2024-06-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_student_choice_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Course_ID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
