# Generated by Django 5.1.3 on 2024-11-13 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='data_final',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='order',
            new_name='ordem',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='tarefa',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='cost',
            new_name='valor',
        ),
    ]
