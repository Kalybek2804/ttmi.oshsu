# Generated by Django 4.0 on 2021-12-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0006_remove_teacher_zvanie'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='zvanie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
