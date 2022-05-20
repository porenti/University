from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_courses():
    return courses.objects.all()

