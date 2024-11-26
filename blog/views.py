from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Muntasir",
        "date": date(2024, 11, 26),
        "title": "Mountain Hiking",
        "excerpt": """There's nothing like the views you get when hiking in the mountains! Ans I wasn't even prepared for what happened whilst I was enjoying the view!""",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minus quod neque 
            quae dolores explicabo exercitationem, cum voluptatem sed voluptate numquam 
            magnam tenetur perferendis labore aut? Nisi in velit quos dolorem?

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minus quod neque 
            quae dolores explicabo exercitationem, cum voluptatem sed voluptate numquam 
            magnam tenetur perferendis labore aut? Nisi in velit quos dolorem?

            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minus quod neque 
            quae dolores explicabo exercitationem, cum voluptatem sed voluptate numquam 
            magnam tenetur perferendis labore aut? Nisi in velit quos dolorem?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2024, 11, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2024, 11, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post["date"]

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request=request, template_name="blog/index.html", context={"posts": latest_posts})


def posts(request):
    return render(request=request, template_name="blog/all-posts.html", context={"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request=request, template_name="blog/post-detail.html", context={"post": identified_post})