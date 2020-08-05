from django.test import TestCase, Client
from django.urls import reverse
from note.models import Note
from note.forms import NoteForm
from datetime import datetime
from django.forms.models import model_to_dict

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.list_details = reverse('note', kwargs={'pk': 4})
        self.addNote_url = reverse('add_note')
        self.note_one = Note.objects.create(
            title='first title',
            text='My first view test',
        )
        self.note_two = Note.objects.create(
            title='second note',
            text='SUsing django built in unitest for testing my django project',
        )
    
    def test_note_home_GET(self):
        response = self.client.get(self.home_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_note_details_GET(self):
        """Retrieve Note """
        note_dix = Note.objects.create(
            title='first title',
            text='My first view test',
        )
        url = reverse('note', kwargs={'pk': self.note_one.pk})
        
        data = model_to_dict(note_dix)
        response = self.client.get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'note.html')
        
   
    def test_note_details_POST(self):
        """ Adding Notes """
        data = model_to_dict(self.note_one)
        response = self.client.post(self.addNote_url, data=data)
        
        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.note_one.title, 'first title')
        self.assertRedirects(response, self.home_url)
        
    
    def test_edit_note_details_POST(self):
         """ Testing Edit note """
        
         form_data = {
            'title':'first title',
            'text':'My first view test update',
         }
         
         url = reverse('edit_note', kwargs={'pk': self.note_one.pk})
         add_form = NoteForm(data= form_data, instance= self.note_one)
         add_form.save()
         response = self.client.post(url, form_data)
         self.assertEquals(response.status_code, 302)
         self.assertEquals(self.note_one.text, 'My first view test update')
        
    
    def test_delte_note_details_POST(self):
        """ Delete Note Test  """
        
        url = reverse('delete', kwargs={'pk': self.note_two.pk})
        data = model_to_dict(self.note_two)
        response = self.client.post(url, data=data)
        
        self.assertEquals(response.status_code, 302)
        # self.assertEquals(self.note_one, '')
        
        