from django.shortcuts import render, redirect
from . import forms
from . import models


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data = {
        'form': forms.TaskForm(),
        'tasks': models.Task.objects.all()
    }
    return render(request, 'index.html', data)
