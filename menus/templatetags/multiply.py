'''
Created on Jun 15, 2012

@author: hxia
'''
from django import template
register = template.Library()
@register.filter
def multiply(value, arg):
    return (int(value)-1) * int(arg)
