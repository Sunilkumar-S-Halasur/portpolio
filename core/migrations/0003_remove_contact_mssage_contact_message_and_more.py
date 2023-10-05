# Generated by Django 4.1.6 on 2023-10-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='mssage',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
