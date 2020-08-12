from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Testing.. Hello World.</h1> <br> Testing complete..')
