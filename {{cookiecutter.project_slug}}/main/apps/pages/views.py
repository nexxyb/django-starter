from django.views.generic.base import TemplateView
from django.views.generic import  ListView, DetailView, FormView, CreateView
#from .forms import RequestServiceForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

class IndexView(TemplateView):
    template_name= 'pages/index.html'
    
