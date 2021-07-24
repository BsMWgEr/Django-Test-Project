
from django.shortcuts import render


def home_page(request):
    my_title = 'Hello there...'
    return render(request, 'about.html', {"title": my_title})
