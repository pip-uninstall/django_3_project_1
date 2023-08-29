from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Page Women')

def categories(request):
    return HttpResponse('Categories')