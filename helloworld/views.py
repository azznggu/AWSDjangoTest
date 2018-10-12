 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

    def test(self, request):
        return render(request, 'test.html', context=None)
    
