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
    # function to find out whether currently rendering post is in the stored posts session or not
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)   # additional data to specify whether the post is stored for read later or not
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
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)   # additional data to specify whether the post is stored for read later or not
        }
        return render(request=request, template_name="blog/post-detail.html", context=context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        # building the context containing the read later posts fetched from session
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request=request, template_name="blog/stored-posts.html", context=context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")   # trying to access the stored_posts session variable

        # if stored_posts variable not created in the session then create it
        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])   # fetching the post id from the request as it is sent via a hidden input filed

        # append the post_id to the stored_posts
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts   # keeping the selected post into the stored_posts session variable
        return HttpResponseRedirect("/")   # redirecting to the current post detail page
