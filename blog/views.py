from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.


def blog_post_detail_page(request, slug):
    print("DJANGO SAYS", request.method, request.path, request.user)
    # obj = BlogPost.objects.get(slug=slug)
    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #    raise Http404
    # obj = queryset.first()
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    template_name = "blog_post_list.html"
    context = {'object_list': []}
    return render(request, template_name, context)


def blog_post_create_view(request):
    return


def blog_post_retrieve_view(request):
    return


def blog_post_update_view(request):
    return


def blog_post_delete_view(request):
    return

