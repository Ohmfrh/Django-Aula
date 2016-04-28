from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


class NameForm(forms.Form):
    my_default_errors = {
        'required': 'Campo requerido',
        'invalid': 'Valores inválidos'
    }
    your_name = forms.CharField(label='Nombre', max_length=100, error_messages=my_default_errors)
    last_name = forms.CharField(label='Apellidos', max_length=100, error_messages=my_default_errors)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))


    # class SimpleForm(forms.Form):
    #     username = forms.CharField(label="Username", required=True)
    #     password = forms.CharField(
    #         label="Password", required=True, widget=forms.PasswordInput)
    #     remember = forms.BooleanField(label="Remember Me?")
    #
    #     helper = FormHelper()
    #     helper.form_method = 'POST'
    #     helper.add_input(Submit('login', 'login', css_class='btn-primary'))