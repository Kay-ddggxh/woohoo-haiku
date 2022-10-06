from django.shortcuts import render
from django.views import generic
from .models import Home


class HomePage(generic.ListView):
    """
    Temporary model to render base template
    """
    queryset = Home
    template_name = 'base.html'
