from django import forms
from .models import Laboratorio 
from crispy_forms.helper import FormHelper

class LaboratorioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LaboratorioForm, self).__init__(*args, **kwargs)
        #self.fields['ciudad'].widget.attrs['placeholder'] = 'Ingrese ciudad'
        #self.fields['ciudad'].widget.attrs['class'] = 'form-control'

        custom_attrs = {
            'class': 'mb-3',
            'toggle-data': 'mydiv',
        }
        # adds our custom_attrs to each element of the form 
        [self.fields[i].widget.attrs.update(custom_attrs) for i in self.fields]

    class Meta:
        model = Laboratorio
        exclude = []