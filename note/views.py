from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.utils.timezone import datetime
from allauth.account.decorators import verified_email_required #similar to @login_required
# Create your views here.

def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', context={'notes': notes})

@verified_email_required
def addNote(request):
    note = NoteForm()
    
    if request.method == 'POST':
        note =  NoteForm(request.POST)
        if note.is_valid():
            form = note.save()
            return redirect('home')
    else:
        note = NoteForm()
    
    return render(request, 'add_note.html', context={'note': note})

def noteDetails(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note.html', context={'note':note})

def editNote(request, pk):
    note = Note.objects.get(id=pk)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        
        if form.is_valid():
            note = form.save(commit=False)
            note.date_created = datetime.now()
            note.save()
            
            return redirect('home')
    else:
        form = NoteForm(instance=note) 
    
    return render(request, 'edit.html', context={'form': form})

def deleteNote(request, pk):
    note = Note.objects.filter(id=pk)
    
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    
    return render(request, 'delete.html', context={'note': note})