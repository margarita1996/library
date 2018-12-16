from django import forms
from .models import Book, Author
from django.contrib.auth.models import User

class NameForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('surname',)
		
	

class TitleForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title',)
		

class DateForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('date',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('info',)
		
		
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'email')

