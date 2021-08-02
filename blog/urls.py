from django.urls import path
from .views import (
    blog_post_detail_page,
    blog_post_list_view,
    blog_post_create_view,
    blog_post_delete_view,
    blog_post_update_view,
    blog_post_detail_view
)


urlpatterns = [

    path('<int:slug>/', blog_post_detail_page),
    path('<int:slug>/', blog_post_update_view),
    path('<int:slug>/', blog_post_delete_view),
    path('', blog_post_list_view),
]