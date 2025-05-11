from django import forms
from .models import Saving, SavingLogs
from decimal import Decimal

class SavingLogsForm(forms.ModelForm) :
    class Meta : 
        model = SavingLogs
        fields = ['nominal', 'description']

        widgets = {
            'nominal' : forms.NumberInput(
                attrs= {
                    'placeholder' : 'Nominal',
                
                }
            ),
            'description' : forms.Textarea(
                attrs= {
                    'placeholder' : 'Deskripsi'
                }
            )
        }

    def __init__(self, *args, **kwargs) :
        self.saving = kwargs.pop('saving')
        self.collected = kwargs.pop('collected')
        super().__init__(*args, **kwargs)

    def clean_nominal(self):
        nominal = self.cleaned_data.get("nominal")
        log_saving = self.saving.saving_entries.order_by('-datetime').first() 
        if log_saving :
            total = log_saving.total
            if self.data.get('action') == 'ambil' and nominal > total :
                print(self.cleaned_data)
                raise forms.ValidationError('Total tabungan anda tidak cukup untuk diambil')
        else : 
            if self.data.get('action') == 'ambil' and not self.collected :
                raise forms.ValidationError('Total tabungan anda tidak cukup untuk diambil')
            
        return nominal
    