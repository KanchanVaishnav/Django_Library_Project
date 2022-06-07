from msilib import Control
from tkinter import Widget
from attr import attr
from django.core import validators
from django import forms
from enroll.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','isbn','author','category']
        