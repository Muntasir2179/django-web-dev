from django.urls import path
from . import views


urlpatterns = [
    path("", view=views.starting_page, name="starting-page"),
    path("post", view=views.posts, name="posts-page"),
    path("post/<slug:slug>", view=views.post_detail, name="post-detail-page")
]


"""
slug transformer:
It is a builtin django transformer containing words separated by dash (-). For example: post/my-first-post
"""