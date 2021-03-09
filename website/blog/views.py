from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Me',
        'title': 'Blog Post',
        'content': 'Content Test',
        'date_posted': 'March 9, 2021'
    },
    {
        'author': 'You',
        'title': 'Second Blog Post',
        'content': 'Second Content Test',
        'date_posted': 'February 22, 2021'
    },
]

def home(request):
    """
    Homepage for blog app.
    """
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)