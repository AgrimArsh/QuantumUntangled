from django.shortcuts import render
from .models import Article

def home(request):
    """
    Homepage for blog app.
    """
    context = {
        'posts': Article.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """
    About page.
    """
    return render(request, 'blog/about.html')

def tags_home(request):
    """
    Tags home page.
    """
    return render(request, 'blog/tags_home.html')

def tags(request, tag):
    """
    Specific tag page.
    """
    context = {
        'tag': tag,
        'posts': Article.objects.filter(tags__name=tag.capitalize())
    }
    return render(request, 'blog/tags.html', context)
