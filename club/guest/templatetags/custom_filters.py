from django import template

register = template.Library() 

@register.filter(name='read_more')
def read_more(value):
    return value[0:100] + "..."


