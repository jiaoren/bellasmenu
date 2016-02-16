'''
Created on Jul 12, 2012

@author: hxia
'''
from django import template
register = template.Library()
@register.filter
def getrange(value):
    return range(8-int(value))

@register.filter
def getrange12(value):
    return range(12-int(value))

@register.filter
def getrange5(value):
    return range(5-int(value))