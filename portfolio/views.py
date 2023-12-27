from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Competencia, Projeto, Contact, Licenciatura, Mestrado
from .forms import ContactForm

def home_page_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            Contact.objects.create(**contact_form.cleaned_data)
            messages.success(request, "Your message has been sent successfully!")

            # Redirect to the same page using a GET request
            return redirect('portfolio:home_page_view')  # Replace 'home_page_view' with the name of your URL pattern

    else:
        contact_form = ContactForm()

    context = {
        'competencias': Competencia.objects.all(),
        'projetos': Projeto.objects.all(),
        'contact_form': contact_form,
    }

    return render(request, 'portfolio/singlepage.html', context)


def lusofona_page_view(request):
    context = {'licenciaturas': Licenciatura.objects.all()}
    return render(request, 'portfolio/lusofona.html', context)

def ucsd_page_view(request):
    context = {'mestrados': Mestrado.objects.all()}
    return render(request, 'portfolio/ucsd.html', context)