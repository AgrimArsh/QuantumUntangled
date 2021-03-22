from django import template
from django.contrib.auth.models import User
from ..models import Tag

register = template.Library()

@register.simple_tag
def get_all_tags():
    return Tag.objects.all()

@register.simple_tag
def get_all_users():
    return User.objects.all()