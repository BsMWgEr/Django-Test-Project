from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm


def home_page(request):
    my_title = 'Hello there...'
    context = {"title": "my title", "my_list": [1, 2, 3, 4, 5]}
    return render(request, 'home.html', context)


def about_page(request):
    context = {'about.html': 'About'}
    return render(request, "about.html", context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        'title': 'Contact Us',
        "form": form
    }
    return render(request, 'form.html', context)
