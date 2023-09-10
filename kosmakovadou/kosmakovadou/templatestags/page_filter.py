from django import template
from main.models import Page
register = template.Library()

@register.filter
def page_filter(section_id):
    page_list = Page.objects.filter(id=section_id)
    
    context = { 'page_list': page_list }

    return context
