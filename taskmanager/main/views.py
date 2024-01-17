from django.shortcuts import render,redirect,HttpResponse
from.models import Task,Project,Prok
from.forms import TaskForm,ProjectForm,ProkForm
from .forms import MyFileForm
from .models import MyFileUpload
from.forms  import  CreateUserForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate ,logout
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from .models import Pro,Prok
from .forms import SearchForm
from django.core.mail import send_mail
from django.conf import settings
import os


def base(request):
    return render(request,'main/base.html')


def register(request):
      form = CreateUserForm()
      if request.method=='POST':
          form=CreateUserForm(request.POST)
          if form.is_valid():
              form.save()
              user = form.cleaned_data.get('username')
              user = form.cleaned_data.get('password1')
    
              messages.success(request,'Account was created for'" "+ user)
              return redirect('log')

      context ={'form':form}
      return render (request,'main/register.html', context)


def log(request):
      if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            pass1=request.POST.get('password')
            user=authenticate(request,username=username,password=pass1)
            if user is not None:
               auth_login(request,user)
               return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
      form = AuthenticationForm()
      return render(request,'main/log.html',context={"form":form} )


def main(request):
    return render(request,'main/main.html')


def profile(request):
    return render(request,'main/profile.html')


def tasks(request):
    tasks=Task.objects.all()
    return render(request,'main/tasks.html',{'title':'tasks room','tasks':tasks})


def people(request):
    return render(request,'main/people.html')    


def project(request):
     error = ''
     if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
        else:
            error = 'form incorrect'     
     form = ProjectForm()
     context = {
        'form': form,
        'error':error
    }
     project=Project.objects.all()
     return render(request,'main/project.html', context)


def doc(request):
    return render(request,'main/doc.html') 


def upload(request):
    prok=Prok.objects.all()
    return render(request,'main/upload.html',{"prok":prok})


def upload2(request):
    return render(request,'main/upload2.html')


def email(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data={
            name:"name",
            email:"email",
            subject:"subject",
            message:"message",
        }
        message='''
        New message:{}

        From:{}
        ''' .format(data[message], data[email])
        send_mail(subject, message,settings.DEFAULT_FROM_EMAIL, ['beka2004zh@gmail.com' ],)
    return render(request,'main/email.html',{  })


def add(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'form incorrect'     
    form = TaskForm()
    context = {
        'form': form,
        'error':error
    }
    return render(request,'main/add.html',context)


def KOSU(request):
    error=''
    if request.method == "POST":
        form=ProkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload')
        else:
            error='form incorrect'
    form=ProkForm()
    context={
        'form':form,
        'error':error
    }
    return render(request,'main/KOSU.html',context)


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            search_results = Pro.objects.filter(name__icontains=search_query)
            return render(request, 'main.html', {'results': search_results})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})



