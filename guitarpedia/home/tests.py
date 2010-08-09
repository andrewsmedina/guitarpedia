#coding: utf-8
from django.test import TestCase

class HomeViewTest(TestCase):
    
    def test_home(self):
        response = self.client.get('/')
        
        assert u'Guitarpedia.com.br' in response.content