# Generated by Django 4.1.7 on 2023-06-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_myfileupload_pro_prok'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prok',
            name='date',
        ),
        migrations.AddField(
            model_name='prok',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]