from django.shortcuts import render, get_object_or_404
from .models import PriceHistory
from django.http import HttpResponse
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'historical_data/index.html'
    context_object_name = 'prices'
    def get_queryset(self):
        return PriceHistory.objects.order_by('id')[:5]

