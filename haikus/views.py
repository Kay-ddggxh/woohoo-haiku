from django.shortcuts import render
from django.views import generic
from .models import Haiku, Tanka


class HaikuList(generic.ListView):
    model = Haiku
    queryset = Haiku.objects.order_by('-create_date')
    template_name = 'index.html'
    # paginate_by = 10