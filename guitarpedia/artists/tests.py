from django.test import TestCase

from artists.models import Band

class BandModelTest(TestCase):
    
    def test_save_a_band(self):
        band = Band()
        band.name = u'Angra'
        band.website = u'http://angra.net'
        band.save()
        
        band = Band.objects.get(id=band.id)
        
        assert u'Angra' == band.name
        
