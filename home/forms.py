from django import forms

class greetingform(forms.Form):
    name = forms.CharField()