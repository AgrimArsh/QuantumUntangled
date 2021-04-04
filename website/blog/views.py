from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Article, Tag

def home(request):
    """
    Homepage for blog app. Passes all articles in context.
    """
    context = {
        'posts': Article.objects.all().order_by('-date_posted'),
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
    Specific tag page. Uses tag specified by url to fetch corresponding articles.
    """
    context = {
        'tag': Tag.objects.filter(db_name__iexact=tag).first,
        'posts': Article.objects.filter(tags__db_name__iexact=tag).order_by('-date_posted'),
    }
    return render(request, 'blog/tags.html', context)

def users_home(request):
    """
    Users home page. Template uses custome template tag to fetch users.
    """
    return render(request, 'blog/users_home.html')

def users(request, user):
    """
    Specific user page. Uses user specified by url to fetch corresponding articles.
    """
    context = {
        'user': User.objects.filter(username__iexact=user).select_related('profile').first,
        'posts': Article.objects.filter(author__username=user).order_by('-date_posted'),
    }
    return render(request, 'blog/users.html', context)