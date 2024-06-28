from django import forms
from api.models import PDFContent


class PDFUploadForm(forms.Form):
    email = forms.EmailField()
    file = forms.FileField(allow_empty_file=False)


class SaltForm(forms.Form):
    payload = forms.CharField(required=True, label='Payload', widget=forms.Textarea(attrs={'rows': 5, 'cols': 50, 'style': 'height:170px;'}))
    salt_key = forms.CharField(max_length=255, required=True,  label='Salt Key')
    salt_index = forms.IntegerField(required=True,  label='Salt Index')
