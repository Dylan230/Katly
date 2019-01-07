from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.account.models import Account, Work, Group, AddToGroup, WorkResponse

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['rol']

        widgets = {

            'rol': forms.Select(attrs={'class':'custom-select'}),
        }

class AccountWork(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'group', 'archive']

        widgets = {

            'group': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }

class AccountGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control'}),

        }

class AccountAddToGroup(forms.ModelForm):
    class Meta:
        model = AddToGroup
        fields = ['name', 'user_add']

        widgets = {

            'user_add': forms.TextInput(attrs={'class':'form-control'}),

        }

class AccountWorkResponse(forms.ModelForm):
    class Meta:
        model = WorkResponse
        fields = ['user_response', 'title', 'description', 'group', 'archive']

        widgets = {

            'description': forms.Textarea(attrs={'class':'form-control'}),

        }

