from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Homepage for blog app.
    """
    return HttpResponse('<h1>Test - Home Blog</h1>')