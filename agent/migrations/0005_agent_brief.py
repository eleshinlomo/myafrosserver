# Generated by Django 4.2.2 on 2023-07-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0004_alter_agent_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='brief',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
