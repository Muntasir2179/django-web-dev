from django.urls import path
from . import views


urlpatterns = [
    path("", view=views.StartingPageView.as_view(), name="starting-page"),
    path("post", view=views.PostsView.as_view(), name="posts-page"),
    path("post/<slug:slug>", view=views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later", view=views.ReadLaterView.as_view(), name="read-later"),
]


"""
slug transformer:
It is a builtin django transformer containing words separated by dash (-). For example: post/my-first-post
"""