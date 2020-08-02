
from django.test import TestCase
from  note.models import Note
from datetime import datetime

class TestModels(TestCase):
    
    def setUp(self):
        self.note_one = Note.objects.create(
            title='First note',
            text='This is my first note',
            date_created=datetime.now()
        )
    
    def test_NOTE_model_text(self):
        self.assertEquals(self.note_one.text, 'This is my first note')
    
    def test_NOTE_model_text_note_none(self):
        self.assertNotEquals(self.note_one.text, ' ')
    
    def test_NOTE_model_str(self):
        self.assertEquals(str(self.note_one.title), 'First note')
    
    
