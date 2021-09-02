from django import template
from django.utils.safestring import mark_safe
from markdown import Markdown

register = template.Library()

MARKDOWN_INSTANCE = Markdown()


@register.filter(is_safe=True)
def md(content):
    return mark_safe(MARKDOWN_INSTANCE.convert(content))
