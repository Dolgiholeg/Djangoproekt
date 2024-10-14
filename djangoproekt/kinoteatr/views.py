from django.http import HttpResponse
# from .forms import UserRegister
from django.views.generic import TemplateView
from .models import *
from django.shortcuts import render


class Main_page(TemplateView):
    template_name = 'main_page.html'


def fud_view(request):
    fud = Fud.objects.all().values()
    title_page = ['"Лакомства"', '"Съешь меня"', '"Выпей меня"']
    context = {'title_page': title_page, 'fud': fud}
    return render(request, 'fud.html', context)

def fud_page_view(request):
    fud = Fud.objects.all().values()
    titel_page = ['"Лакомства"', '"Съешь меня"', '"Выпей меня"']
    context = {'titel_page': titel_page, 'fud': fud}
    return render(request, 'fud_page.html', context)




