from django import forms


class CreateForm(forms.Form):
	kitapId = forms.IntegerField()
        name = forms.CharField(max_length=255)
        sayfa_sayisi = forms.IntegerField()
        yazar_adi = forms.CharField(max_length=255)
