from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from IPython import embed
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = Movie()
            movie.title = form.cleaned_data.get('title')
            movie.title_en = form.cleaned_data.get('title_en')
            movie.audience = form.cleaned_data.get('audience')
            movie.open_date = form.cleaned_data.get('open_date')
            movie.genre = form.cleaned_data.get('genre')
            movie.watch_grade = form.cleaned_data.get('watch_grade')
            movie.score = form.cleaned_data.get('score')
            movie.poster_url = form.cleaned_data.get('poster_url')
            movie.description = form.cleaned_data.get('description')
            movie.save()

            return redirect('movies:index')
        else:
            pass
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'form.html', context)


def detail(request, id):
    # movie = Movie.objects.get(id=id)
    movie = get_object_or_404(Movie, id=id)
    context = {
        "movie": movie
    }
    return render(request, 'detail.html', context)


def delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect("movies:detail")


def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        pass
    else:
        form = MovieForm(initial=movie.__dict__)
    context = {
        'form': form
    }
    return render(request, 'form.html', context)
