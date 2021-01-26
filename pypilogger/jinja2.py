from django.templatetags.static import static
from django.urls import reverse
from django.contrib import messages
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'messages': messages,
    })
    return env
