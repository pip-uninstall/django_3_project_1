from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *


# Create your views here.
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html')

def about(request):
    return render(request, 'women/about.html')


def categories(request, catid):
    if request.POST:
        return HttpResponse('Categories')


def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=True)



def pageNotFound(request, exception):
    return HttpResponseNotFound('404')
