from django.urls import path, include
from django.conf import settings

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/profile/', home, name='profile'),
    path('add_note/', addNote, name='add_note'),
    
    path('note/<str:pk>/', noteDetails, name='note'),
    path('note/<str:pk>/delete', deleteNote, name='delete'),
    
    path('edit/<str:pk>/', editNote, name='edit_note'),
    
]

