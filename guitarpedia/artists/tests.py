#coding: utf-8
from django.test import TestCase
from datetime import datetime
from artists.models import Band, Guitarrist

class BandModelTest(TestCase):
    
    def test_save_a_band(self):
        band = Band()
        band.name = u'Angra'
        band.website = u'http://angra.net'
        band.save()
        
        band = Band.objects.get(id=band.id)
        
        assert u'Angra' == band.name
        

class GuitarristModelTest(TestCase):
    
    def test_save_a_guitarrist(self):
        guitarrist = Guitarrist()
        guitarrist.name = u'Kiko Loureiro'
        guitarrist.website = u'http://www.kikoloureiro.com.br'
        guitarrist.biography = u'''Pedro Henrique Loureiro, mais conhecido 
            como Kiko Loureiro (Rio de Janeiro, 16 de Junho de 1972), é 
            guitarrista da banda brasileira de metal melódico/power metal 
            Angra e professor da Escola de Música e Tecnologia - EM&T, no 
            Instituto de Guitarra e Tecnologia - IG&T, em São Paulo'''
        guitarrist.date_of_birthday = datetime(1972, 06, 16)
            
        guitarrist.save()
        
        guitarrist = Guitarrist.objects.get(id=guitarrist.id)
        
        assert u'Kiko Loureiro' == guitarrist.name
        
class GuitarristViewTest(TestCase):
    
    def setUp(self):
        guitarrist = Guitarrist()
        guitarrist.name = u'Kiko Loureiro'
        guitarrist.website = u'http://www.kikoloureiro.com.br'
        guitarrist.biography = u'''Pedro Henrique Loureiro, mais conhecido 
            como Kiko Loureiro (Rio de Janeiro, 16 de Junho de 1972), é 
            guitarrista da banda brasileira de metal melódico/power metal 
            Angra e professor da Escola de Música e Tecnologia - EM&T, no 
            Instituto de Guitarra e Tecnologia - IG&T, em São Paulo'''
        guitarrist.date_of_birthday = datetime(1972, 06, 16)
            
        guitarrist.save()
        
        self.guitarrist = guitarrist
        
    def tearDown(self):
        Guitarrist.objects.all().delete()
    
    def test_guitarrist_list(self):
        response = self.client.get('/guitarrists/')
        assert u'Kiko Loureiro' in response.content
