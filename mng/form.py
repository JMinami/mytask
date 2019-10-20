from django import forms
from django.forms import ModelForm
from mng.models import task, progress


class taskForm(ModelForm):
    class Meta:
        model = task
        #fields = ('level',)
        fields = '__all__'


class progress(ModelForm):
   class Meta:
      model = progress
      fields = '__all__'