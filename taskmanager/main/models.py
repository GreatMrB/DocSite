from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,User
from datetime import date


class Pro(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Task(models.Model):
    title=models.CharField('Название', max_length=200)
    task=models.TextField('Описание')


    def __str__(self):
        return self.title


class Prok(models.Model):
    title=models.CharField('Название', max_length=200)
    work=models.CharField('Ответственный', max_length=200)
    name=models.CharField('ФИО',max_length=200)
    job=models.CharField('Должность',max_length=200)
    datetime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



class Project(models.Model):
    title=models.CharField('Название', max_length=200)
    project=models.TextField('Описание')


    def __str__(self):
        return self.title
    


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Profile')
    image=models.ImageField(upload_to='pics', default='default.svg')


    def __str__(self):
        return f'{self.user} Profile'



class MyFileUpload(models.Model):
    file_name=models.CharField(max_length=50)
    my_file=models.FileField()