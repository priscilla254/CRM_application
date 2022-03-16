from django.shortcuts import render
from django.template import RequestContext,loader
from .models import Note
from .forms import *
def take_notes(request):
    notes=Note.objects.all()
    template=loader.get_template('notes/note.html')
    form=NoteForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()

    context={'notes':notes,'form':form}
    return render(request,"notes/note.html",context)
