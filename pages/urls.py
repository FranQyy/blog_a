from django.urls import path
from . import views

app_name='pages'

urlpatterns = [
  path('', views.index, name='index'),
  path('o-nas', views.o_nas, name='o_nas'),
  path('uslugi', views.uslugi, name='uslugi'),
  path('uslugi/referencje/<int:id>/<str:slug>', views.referencja, name='referencja'),
  path('aktualnosci', views.aktualnosci, name='aktualnosci'),
  path('aktualnosci/wpis/<int:id>/<str:slug>', views.wpis, name='wpis'),
  path('kontakt', views.kontakt, name='kontakt'),

]