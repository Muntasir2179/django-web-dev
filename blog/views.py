from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]   # fetch all post from database and order them in descending order
    return render(request=request, template_name="blog/index.html", context={"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")   # fetch all post from database and order them in descending order
    return render(request=request, template_name="blog/all-posts.html", context={"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)   # filter post from database using slug. Note: if slug is not correct this will render 404 page
    # identified_post = Post.objects.filter(slug__contains=slug)[0]   # filter post from database using slug. Note: if slug is not correct this will fail
    return render(request=request, 
                  template_name="blog/post-detail.html", 
                  context={
                      "post": identified_post,
                      "post_tags": identified_post.tags.all()
                  })