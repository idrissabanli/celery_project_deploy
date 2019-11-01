from django import template

register = template.Library()

@register.simple_tag
def split_str(split_s, value):
    return split_s.split(value)