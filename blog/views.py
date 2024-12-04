from django.views.generic import ListView, DetailView

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


class SinglePostView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    # context_object_name = "post"  # context_object_name is automatically set to post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()   # self.object holds the single Post model object
        context['comment_form'] = CommentForm()
        return context
