from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from portfolio.models import Competencia, Projeto, Contact
from .forms import ContactForm

def home_page_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            Contact.objects.create(**data)
            send_mail(
                subject=f"Portfolio Contact: {data['subject']}",
                message=f"From: {data['name']} <{data['email']}>\n\n{data['message']}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('portfolio:home_page_view')
    else:
        contact_form = ContactForm()

    context = {
        'competencias': Competencia.objects.all(),
        'projetos': Projeto.objects.all(),
        'contact_form': contact_form,
    }

    return render(request, 'portfolio/singlepage.html', context)
