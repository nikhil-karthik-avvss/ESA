# Generated by Django 3.2.18 on 2024-06-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_student_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Previous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rank', models.IntegerField()),
                ('CutOff', models.IntegerField()),
                ('College', models.TextField()),
                ('Course', models.TextField()),
            ],
        ),
    ]
