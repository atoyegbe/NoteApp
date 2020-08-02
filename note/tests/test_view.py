from django.test import TestCase, Client
from django.urls import reverse
from note.models import Note
from datetime import datetime
from django.forms.models import model_to_dict

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.list_details = reverse('note', args=[4])
        self.note_one = Note.objects.create(
            title='first title',
            text='My first view test',
            date_created=datetime.now()
        )
        
    
    def test_note_home_GET(self):
        response = self.client.get(self.home_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_note_details_GET(self):
        data = model_to_dict(self.note_one)
        response = self.client.get(self.list_details, data=data)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'note.html')
        
   
