from django.shortcuts import render
from .models import Article

def home(request):
    """
    Homepage for blog app.
    """
    context = {
        'posts': Article.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """
    About page.
    """
    return render(request, 'blog/about.html')