from django import template

register = template.Library()

@register.filter(name="floatvar")
def floatvar(var):
    return float(var)