from django import  template
register=template.Library()

def swap(value):
    return value.swapcase()

register.filter('swapping',swap)

@register.filter('counts')
def counting(value,arg):
    c=0
    for ip in range(len(value)):
        if arg==value[ip:len(arg)+ip:]:
            c+=1
    return c

@register.filter()
def removing(value,arg):
    return value.replace(arg,'')

@register.filter()
def reversed(value):
    return value[::-1]


    
    