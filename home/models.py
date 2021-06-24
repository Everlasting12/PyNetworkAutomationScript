from django.db import models
from django import forms
from django.forms import ModelForm



class Contact(models.Model):
    uname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=2000)
    date = models.DateField()

    def __str__(self):
        return self.uname + "  |  "+ self.email

class Script(models.Model):
    script_name = models.CharField(max_length=50)
    script_author = models.CharField(max_length=30)
    script_file = models.FileField(upload_to='media')
    description = models.TextField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.script_name

class Tutorial(models.Model):
    script_name = models.ForeignKey("home.Script",  on_delete=models.CASCADE)
    prerequisite = models.TextField()
    steps = models.TextField()
    date = models.DateTimeField()  

    def __str__(self):
        return str(self.script_name)  