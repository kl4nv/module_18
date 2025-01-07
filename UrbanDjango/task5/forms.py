from django import forms

class UserRegistr(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин: ')
    password = forms.PasswordInput()
    repeat_password = forms.PasswordInput()
    age = forms.CharField(max_length=3, label='Введите свой возраст: ')
