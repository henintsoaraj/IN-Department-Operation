from django import template
from django.utils.safestring import mark_safe


"""@register.filter()
def nbsp(value):
    return mark_safe("&nbsp;&nbsp;&nbsp;".join(value.split(' ')))
"""
register = template.Library()

@register.filter()
def is_numeric(value):
    if isinstance(value, int):
        return value