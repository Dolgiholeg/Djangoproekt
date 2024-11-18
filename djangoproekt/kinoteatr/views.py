from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def start_page_view(request):
    return render(request, 'start_page.html')


def main_page_view(request):
    return render(request, 'main_page.html')


def fud_view(request):
    a_treat = A_treat.objects.all()  # type: ignore
    pizza = Pizza.objects.all()  # type: ignore
    drinks = Drinks.objects.all()  # type: ignore
    title_page_fud = ["Лакомства", "Съешь меня", "Выпей меня"]
    context = {'title_page_fud': title_page_fud, 'a_treat': a_treat, 'pizza': pizza, 'drinks': drinks}
    return render(request, 'fud.html', context)


def today_view(request):
    today = Today.objects.all()  # type: ignore
    title_page_today = "Посмотри меня"
    context = {'title_page_today': title_page_today, 'today': today}
    return render(request, 'today.html', context)


def multfilm_view(request):
    film = Film.objects.filter(id=1)  # type: ignore
    acter = Acter.objects.filter(film_acter=1)  # type: ignore
    foto_film = Foto_film.objects.filter(film=1)  # type: ignore
    context = {'film': film, 'acter': acter, 'foto_film': foto_film}
    return render(request, 'multfilm.html', context)


def film1_view(request):
    film = Film.objects.filter(id=2)  # type: ignore
    acter = Acter.objects.filter(film_acter=2)  # type: ignore
    foto_film = Foto_film.objects.filter(film=2)  # type: ignore
    context = {'film': film, 'acter': acter, 'foto_film': foto_film}
    return render(request, 'film1.html', context)


def film2_view(request):
    film = Film.objects.filter(id=3)  # type: ignore
    acter = Acter.objects.filter(film_acter=3)  # type: ignore
    foto_film = Foto_film.objects.filter(film=3)  # type: ignore
    context = {'film': film, 'acter': acter, 'foto_film': foto_film}
    return render(request, 'film2.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    context = {'form': form }
    return render(request, 'registration.html', context)


def comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comments')
    else:
        form = CommentForm()
    comments = Comment.objects.all()  # type: ignore
    return render(request, 'comments.html', {'form': form, 'comments': comments })

