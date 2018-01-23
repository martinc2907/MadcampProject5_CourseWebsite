from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	# This is just info about class 
	class Meta:
		model = User
		fields = ['username', 'email', 'password']