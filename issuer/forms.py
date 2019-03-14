from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Credential


class PersonForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.CharField(label='Email')


class CredentialForm(forms.Form):
    title = forms.CharField(label='Title')
    description = forms.CharField(label='Description')
    narrative = forms.CharField(label='Narrative')
    issuing_department = forms.CharField(label='Issuing Department')


class IssuanceForm(forms.Form):
    credentials = Credential.objects.values_list('id', 'title')
    credential = forms.CharField(label='Credential', widget=forms.Select(choices=credentials))
    date_issue = forms.DateField(label='Issue Date', widget=DatePickerInput())