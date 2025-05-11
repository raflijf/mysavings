from django import template
from main.models  import Saving


register = template.Library()

@register.simple_tag
def status(id_saving) :
    saving = Saving.objects.get(id = id_saving )
    status = saving.saving_entries.all().order_by('-datetime').first()
    return status

@register.simple_tag
def gap(target, collected) :
    return target - collected

