from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = 'Hello there...'
    context = {"title": "my title", "my_list": [1, 2, 3, 4, 5]}
    
    return render(request, 'home.html', context)


def about_page(request):
    context = {'about.html': 'About'}
    return render(request, "about.html", context)


def contact_page(request):
    context = {'title': 'Contact'}
    return render(request, 'contact.html', context)


def example_page(request):
    context = {"title": "Example"}
    template_name = "home.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)