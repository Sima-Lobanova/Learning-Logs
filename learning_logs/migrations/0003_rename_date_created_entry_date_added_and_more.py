# Generated by Django 5.0.6 on 2024-06-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_created',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='date_created',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
