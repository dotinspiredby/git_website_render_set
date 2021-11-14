import os

from django import template


register = template.Library()


@register.filter
def href_filename(value):
    return "#" + str(value)


@register.filter
def filename(value):
    return str(value)


@register.filter
def href_bio(value):
    return "/bio/" + value
