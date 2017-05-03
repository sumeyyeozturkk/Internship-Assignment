from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    sayfa_sayisi = forms.IntegerField()
    yazar_adi = forms.CharField(max_length=255)
