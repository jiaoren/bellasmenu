'''
Created on Jun 15, 2012

@author: hxia
'''
from django import template
register = template.Library()
@register.filter
def modeandmultiply(value, arg):
    return ((int(value)-1) % 7)*int(arg)