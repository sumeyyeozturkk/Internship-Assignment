# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from mongoengine import *
from .models import Kitap
from .forms import CreateForm

def create(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			kitapId = form.cleaned_data["kitapId"]
			name = form.cleaned_data["name"]
			sayfa_sayisi = form.cleaned_data["sayfa_sayisi"]
			yazar_adi = form.cleaned_data["yazar_adi"]
			Kitap.objects.create(kitapId=kitapId, name=name, sayfa_sayisi=sayfa_sayisi, yazar_adi=yazar_adi)
			return HttpResponse("EKLENDİ")
	else:
		form = CreateForm()
		return render(request, 'create_form.html', {'form': form})

def list(request):
    kitaplar = Kitap.objects.fields().values_list()
    return render(request, 'index.html', {'data': kitaplar})


def delete(request, kitapId=''):
	obje = Kitap.objects.get(kitapId=kitapId)
	obje.delete()
	return HttpResponse('Silindi')
	
def edit(request, kitapId=''):
	if request.method == 'POST':
		form = CreateForm(request.POST)
                if form.is_valid():
			kitapId = form.cleaned_data["kitapId"]
                        name = form.cleaned_data["name"]
                        sayfa_sayisi = form.cleaned_data["sayfa_sayisi"]
                        yazar_adi = form.cleaned_data["yazar_adi"]
                        Kitap.objects.create(kitapId=kitapId, name=name, sayfa_sayisi=sayfa_sayisi, yazar_adi=yazar_adi)
                        return HttpResponse("EKLENDİ")

		return render(request, 'edit_forms.html', {'form': form})
	else:	
		info = {}
		obje = Kitap.objects.get(kitapId=kitapId)
		info["kitapID"] = obje.kitapId	
		info["name"] = obje.name
		info["yazar_adi"] = obje.yazar_adi
		info["sayfa_sayisi"] = obje.sayfa_sayisi
		form = CreateForm(data=info)
		return render(request, 'edit_forms.html', {'form': form})
