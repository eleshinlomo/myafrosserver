# Generated by Django 4.2.2 on 2023-07-07 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_alter_agent_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'ordering': ('id',)},
        ),
    ]
