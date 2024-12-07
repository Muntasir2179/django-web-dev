from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post
from .forms import CommentForm


# Create your views here.

class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]   # fetch all post from database and order them in descending order by date and taking first 3 posts


class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request=request, template_name="blog/post-detail.html", context=context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)   # by setting commit=False we are not hitting database instead we are creating a instance of a model
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request=request, template_name="blog/post-detail.html", context=context)

