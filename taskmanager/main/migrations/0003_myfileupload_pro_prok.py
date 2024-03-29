# Generated by Django 4.1.7 on 2023-06-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('my_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('work', models.CharField(max_length=200, verbose_name='Ответственный')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('job', models.CharField(max_length=200, verbose_name='Должность')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
