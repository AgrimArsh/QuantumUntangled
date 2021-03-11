from django import template
from ..models import Tag

register = template.Library()

@register.simple_tag
def get_all_tags():
    return Tag.objects.all()