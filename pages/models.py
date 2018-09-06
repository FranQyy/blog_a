from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Referencja(models.Model):    
  nazwa = models.CharField(max_length=50)
  slug = models.SlugField(max_length=100, unique_for_date='publish')
  logo = models.ImageField(upload_to='pracownik/%y/%m/%d', blank=True)
  skan = models.ImageField(upload_to='pracownik/%y/%m/%d', blank=True)
  publish = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ('-publish',)
    verbose_name_plural = "Referencje"

  def __str__(self):
    return self.nazwa

  def get_absolute_url(self):
    return reverse('pages:referencja', args=[self.id, self.slug])

class Wpis(models.Model):
  temat = models.CharField(max_length=250)
  tekst = models.TextField()
  slug = models.SlugField(max_length=100, unique_for_date='date_added')
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'wpisy'

  def __str__(self):
    return self.tekst[:50] + '...'

  def get_absolute_url(self):
    return reverse('pages:wpis', args=[self.id, self.slug])