# -*- coding: utf-8 -*-
from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, help_text='Имя', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.EmailField(help_text='email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваш запрос'}))
    phone = forms.CharField(max_length=50, help_text='Ваш номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}))