from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from blog.models import Cat, Dog, Team
from blog.forms import AddCatForm, AddDogForm


def home(request):
    return render(request, 'blog/main.html')


class ListKittens(ListView):
    model = Cat
    queryset = Cat.objects.all()


class ListPupies(ListView):
    model = Dog
    queryset = Dog.objects.all()


class DetailKit(View):
    def get(self, request, pk):
        data = Cat.objects.get(id=pk)
        return render(request, 'blog/pet.html', {'pet': data})


class DetailPup(View):
    def get(self, request, pk):
        data = Dog.objects.get(id=pk)
        return render(request, 'blog/pet.html', {'pet': data})


def AboutUs(request):
    return render(request, 'blog/about_us.html')


def OftenQuest(request):
    return render(request, 'blog/often_questions.html')


class TeamList(ListView):
    model = Team
    queryset = Team.objects.all()
    template_name = 'blog/about_us.html'


def AddCat(request):
    if request.method == 'POST':
        form = AddCatForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cat')

    else:
        form = AddCatForm()
    return render(request, 'blog/addcat.html', {'form': form})


def AddDog(request):
    if request.method == 'POST':
        form = AddDogForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dog')

    else:
        form = AddDogForm()
    return render(request, 'blog/adddog.html', {'form': form})
