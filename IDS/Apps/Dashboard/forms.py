from django import forms
from .models import files

class files_form(forms.ModelForm):
    class Meta:
        model = files
        fields = ( 'file_name' , 'describe' , )
