from django.shortcuts import render, redirect
from .models import Taski
from .forms import TaskiForm


def index(request):
    taski = Taski.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страциа сайта', 'taski': taski})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskiForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
