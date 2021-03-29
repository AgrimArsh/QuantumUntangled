from django.contrib import admin
from .models import Article, Tag, Profile

admin.site.register([Article, Tag, Profile])
