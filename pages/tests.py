from django.test import TestCase
from pages.models import Pracownik

# Create your tests here.
class PracownikTest(TestCase):
  def setUp(self):
    Pracownik.objects.create(first_name='Adam', last_name='Kowalski')
    Pracownik.objects.create(first_name='Tomek', last_name='Nowak')

  def test_string_representation(self):
    pracownik_name_1 = Pracownik.objects.get(first_name='Adam')
    pracownik_name_2 = Pracownik.objects.get(first_name='Tomek')
    self.assertEqual(str(pracownik_name_1), 'Kowalski Adam')    
    self.assertEqual(str(pracownik_name_2), 'Nowak Tomek')    

  def test_verbose_name_plural(self):
    self.assertEqual(str(Pracownik._meta.verbose_name_plural), "Pracownicy")

  