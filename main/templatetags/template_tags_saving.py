from django import template
from main.models  import Saving
from decimal import Decimal

register = template.Library()

@register.simple_tag
def status(id_saving) :
    saving = Saving.objects.get(id = id_saving )
    status = saving.saving_entries.all().order_by('-datetime').first()
    return status


def safe_int(value):
    # Jika value adalah None atau string kosong, kembalikan 0
    if value in (None, ''):
        return 0
    try:
        # Coba konversi ke integer
        return int(value)
    except ValueError:
        # Jika terjadi error konversi, kembalikan 0
        return 0

@register.simple_tag
def gap(target, collected) :
    return safe_int(target) - safe_int(collected)

