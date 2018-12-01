from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def home(request):
	return render(request, 'home/home.html')

def hehe(request):
    return render(request, 'home/hehe.html')

class greeting(TemplateView):
    template_name = 'home/greeting.html'

    def get(self, request):
        form = forms.greetingform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = forms.greetingform(request.POST)
        if form.is_valid():
            text = form.cleaned_data['name']

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)