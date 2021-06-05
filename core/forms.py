from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from core.models import Plant


class PlantForm(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Сохранить', css_class='btn-primary'))
    helper.form_method = 'POST'

    class Meta:
        model = Plant
        fields = '__all__'
