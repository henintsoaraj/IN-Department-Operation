from django import template
from django.utils.safestring import mark_safe


"""@register.filter()
def nbsp(value):
    return mark_safe("&nbsp;&nbsp;&nbsp;".join(value.split(' ')))
"""
register = template.Library()

@register.filter()
def color1(text):
    textFind = "responseCode</name><value><i4>"
    try:
        idx = text.index(textFind)
        textFormat = text[:(idx + len(textFind))]
        return textFormat
    except ValueError:
        print("no")


@register.filter()
def color2(text):
    textFind = "responseCode</name><value><i4>"
    try:
        idx = text.index(textFind)
        textFormat = text[(idx+len(textFind)):(idx+len(textFind))+1]
        return textFormat
    except ValueError:
        print("no")

@register.filter()
def color3(text):
    textFind = "responseCode</name><value><i4>"
    try:
        idx = text.index(textFind)
        textFormat = text[((idx + len(textFind)) + 1):]
        return textFormat
    except ValueError:
        print("no")
