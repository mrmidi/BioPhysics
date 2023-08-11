from django import template

register = template.Library()


@register.filter
def sequence(value, end):
    return range(value, end)