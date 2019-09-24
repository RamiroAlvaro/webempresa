from django import template
from webempresa.pages.models import Page

register = template.Library()


@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
