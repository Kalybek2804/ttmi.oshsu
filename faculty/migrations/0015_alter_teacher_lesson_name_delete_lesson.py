# Generated by Django 4.0 on 2021-12-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0014_alter_teacher_lesson_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='lesson_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]