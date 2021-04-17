from django.forms import ModelForm
from django import forms
from apps.models import Users_tb, Skill_tb

class FormUser(ModelForm):
    class Meta:
        model = Users_tb
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput({'class':'form-control'}),
            'photo' : forms.ClearableFileInput({'class':'form-control'}),
        }

class FormSkill(ModelForm):
    class Meta:
        model = Users_tb
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput({'class':'form-control'}),
        }