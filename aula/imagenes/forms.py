from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from imagenes.models import Server, Image

class AddImage(forms.Form):
    Name = forms.CharField(required=True, label='Nombre del archivo')
    ServerList = forms.ModelChoiceField(required=True, queryset=Server.objects.all())
    Path = forms.CharField(required=True, label='Path')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/imagenes/agregar/'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))


class ImageForm(forms.Form):
    Imagenes = forms.ModelMultipleChoiceField(queryset=Image.objects.all(), widget=forms.CheckboxSelectMultiple)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/imagenes/editar/'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))
    helper.layout = Layout(
        Field('Imagenes', css_class="checkbox-inline"),
    )
    helper.html5_required = False
