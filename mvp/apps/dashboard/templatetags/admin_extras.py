from django import template

register = template.Library()


@register.filter(name="cut")
def incident_severity(value, arg):
    return value + ":D"
