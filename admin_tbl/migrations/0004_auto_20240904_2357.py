# Generated by Django 5.0.4 on 2024-09-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_tbl', '0003_auto_20240904_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson', models.ForeignKey(to="Student", on_delete=models.CASCADE)),
                ('times', models.IntegerField()),
                ('progress', models.IntegerField()),
                ('memo', models.TextField()),
            ],
        ),
    ]
