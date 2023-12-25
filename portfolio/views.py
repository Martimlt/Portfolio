from django.shortcuts import render
from portfolio.models import Cadeira, Pessoa, Projeto, Competencia

# Create your views here.

def home_page_view(request):
    context = {'competencias': Competencia.objects.all(), 'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/singlepage.html', context)

def lusofona_page_view(request):
    return render(request, 'portfolio/lusofona.html')

def ucsd_page_view(request):
    return render(request, 'portfolio/ucsd.html')