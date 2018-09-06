from django.shortcuts import render, get_object_or_404
from .models import Referencja, Wpis

def index(request):
  return render(request, 'pages/content/index.html')

def o_nas(request):
  referencje = Referencja.objects.all()
  context = {'referencje': referencje}
  return render(request, 'pages/content/o_nas.html', context)

def uslugi(request):
  return render(request, 'pages/content/uslugi.html')

def referencja(request, id, slug):
  referencja = get_object_or_404(Referencja, id=id, slug=slug)
  context = {'referencja': referencja}
  return render(request, 'pages/content/referencja.html', context)

def aktualnosci(request):
  wpisy = Wpis.objects.all()
  context = {'wpisy': wpisy}
  return render(request, 'pages/content/aktualnosci.html', context)

def wpis(request, id, slug):
  wpis = get_object_or_404(Wpis, id=id, slug=slug)
  context = {'wpis': wpis}
  return render(request, 'pages/content/wpis.html', context)

def kontakt(request):
  return render(request, 'pages/content/kontakt.html')
