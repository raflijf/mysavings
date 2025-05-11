from django import template
from translate import Translator

register = template.Library()

translator = Translator(to_lang='id')

@register.filter
def translate(value) :
    return translator.translate(value)