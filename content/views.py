from django.shortcuts import render
from django.http import HttpResponse


def contentDataBase(request):
    return HttpResponse('<h1>Hello content</h1>')
