from django.test import TestCase

from note.forms import NoteForm



class TestForm(TestCase):
    
    def test_NOTE_FORM(self):
        form = NoteForm(data={
            "title": "First note",
            "text": "My first unit test"
        })
        
        self.assertTrue(form.is_valid())
    
    def test_NOTE_FORM_no_data(self):
        form = NoteForm(data={})
        
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)