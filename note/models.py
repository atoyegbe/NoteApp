from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50, default='Unknown Title')
    text = RichTextUploadingField()
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'notes'
    
    def __str__(self):
        return self.title
    