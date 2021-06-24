# from django import views
from django import forms
from django.forms import ModelForm
from .models import Script, Tutorial

# queryset=Script.objects.all()

class TutorialRegistration(forms.Form):
    scriptName = forms.ModelChoiceField(queryset=Script.objects.all(), label="Script Name:", widget=forms.Select(attrs={'class':'form-control w-75'}), required=True)
    preRequisites = forms.CharField(label="Prerequisites :",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Prerequisites','rows':'3'}))
    Steps = forms.CharField(label="Steps :",widget=forms.Textarea(attrs = {'class':'form-control','placeholder':'List all the Steps','rows':'9'}))


# class ScriptFormRegistration(forms.Form):
#     Script_Name = forms.CharField(label="Script Name :", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Script Name'}))
#     Script_Description = forms.CharField(label="Script Description :", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Script Description here, less than 500 characters.','rows':'3'}),max_length=500,min_length=10)
#     Script_File = forms.FileField(label="Browse Script File :", widget=forms.FileInput(attrs={'class':'form-control p-1'}))
#     Author_Name = forms.CharField(label="Author Name :", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Script Name'}))

class ScriptFormRegistration(forms.ModelForm):
    class Meta:
        model = Script
        fields = ['script_name','description','script_file','script_author']
        widgets={
            'script_name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'script_file':forms.FileInput(attrs={'class':'form-control p-1'}),
            'script_author':forms.TextInput(attrs={'class':'form-control'}),
        }