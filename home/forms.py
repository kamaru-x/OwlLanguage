from django import forms
from django.forms import TextInput,Textarea,FileInput
from home.models import Blog,About
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import PasswordChangeForm

class Edit_Blog(forms.ModelForm):
    class Meta():
        model = Blog
        fields = '__all__'

class AboutForm(forms.ModelForm):
    Description = forms.CharField(widget=CKEditorWidget())
    class Meta():
        model = About
        fields = ('Title','Description','Image','Url','SMTitle','SMDescription','SMKeywords','Mission','Vision')

        widgets = {
            'Title': TextInput(attrs={'class' : 'form-control','name' : 'title','id':'title'}),
            'Image' : FileInput(attrs={'class' : 'form-control'}),
            'Description' : Textarea(attrs={'class':'form-control'}),
            'Url' : TextInput(attrs={'class' : 'form-control','name' : 'url','id':'url'}),
            'SMTitle' : TextInput(attrs={'class' : 'form-control'}),
            'SMKeywords' : TextInput(attrs={'class' : 'form-control'}),
            'SMDescription' : Textarea(attrs={'class' : 'form-control'}),
            'Mission' : Textarea(attrs={'class' : 'form-control'}),
            'Vision' : Textarea(attrs={'class' : 'form-control'}),
        }

class ChangePassword(PasswordChangeForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for fieldname in ['old_password','new_password1','new_password2'] :
            self.fields[fieldname].widget.attrs = {'class' : 'form-control'}