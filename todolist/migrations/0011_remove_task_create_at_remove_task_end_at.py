# Generated by Django 4.2.18 on 2025-01-22 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_alter_subtask_progress_score_alter_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='end_at',
        ),
    ]
