from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def megha(request):
    return HttpResponse('My Name is Megha')

def kee(request):
    return HttpResponse('<marquee>My name is Kee and Megha is my sister</marquee>')

