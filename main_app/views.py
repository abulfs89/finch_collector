from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from .models import finches

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finches = finch.objects.get(id=finch_id)
  return render (request, 'finches/detail.html', {'finch' : finches})

class finchCreate(CreateView):
    model = finch
    fields = '__all__'
    success_url = '/finches'

class finchUpdate(UpdateView):
  model = finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class finchDelete(DeleteView):
  model = finch
  success_url = '/finches'
