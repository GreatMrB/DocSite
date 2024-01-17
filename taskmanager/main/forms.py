from.models import Task, Project,Prok
from django.forms import ModelForm, TextInput,Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search')


class TaskForm (ModelForm):
    class Meta:
        model = Task
        fields = ["title", 'task']
        widgets = {
        'title': TextInput(attrs={
            'class': 'input',
            'placeholder':'Task'
        }),
        'task': Textarea(attrs={
            'class': 'textarea',
            'placeholder': 'Description'
        }),


        
        }


class ProkForm(ModelForm):
    class Meta:
        model=Prok
        fields=["title",'work','name','job']
        widgets={
             'title': TextInput(attrs={
            'class': 'input',
            'placeholder':'title'
        }),
         'work': TextInput(attrs={
            'class': 'input',
            'placeholder':'Task'
        }),
         'name': TextInput(attrs={
            'class': 'input',
            'placeholder':'name'
        }),
         'job': TextInput(attrs={
            'class': 'input',
            'placeholder':'job'
        }),

        }


class ProjectForm (ModelForm):
    class Meta:
        model = Project
        fields = ["title"]
        widgets = {
        'title': TextInput(attrs={
            'class': 'input',
            'placeholder':'Project'
        }),



        
       


        
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email','password1','password2']




class MyFileForm(forms.Form):
    file_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))