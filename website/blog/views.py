from django.shortcuts import render
from .models import Article

def home(request):
    """
    Homepage for blog app. Passes all articles in context.
    """
    context = {
        'posts': Article.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """
    About static page.
    """
    return render(request, 'blog/about.html')

def tags_home(request):
    """
    Tags home page. Template uses custom template tag to fetch available tags.
    """
    return render(request, 'blog/tags_home.html')

def tags(request, tag):
    """
    Specific tag page. Uses tag specified by the url to fetch corresponding articles.
    """
    context = {
        'tag': tag,
        'posts': Article.objects.filter(tags__name=tag.capitalize())
    }
    return render(request, 'blog/tags.html', context)
