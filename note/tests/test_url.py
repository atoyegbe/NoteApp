from django.test import SimpleTestCase
from django.urls import reverse, resolve
from note.views import home, addNote, noteDetails, editNote, deleteNote

class TestUrls(SimpleTestCase):
    
    def test_url_add_note_resolved(self):
        url = reverse('add_note')
        self.assertEquals(resolve(url).func, addNote)
    
    def test_url_home_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_url_note_details_resolved(self):
        url = reverse('note', args=[2])
        self.assertEquals(resolve(url).func, noteDetails)
    
    def test_url_edit_note_resolved(self):
        url = reverse('edit_note', args=[2])
        self.assertEquals(resolve(url).func, editNote)
    
    def test_url_edit_note_resolved(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func, deleteNote)
    