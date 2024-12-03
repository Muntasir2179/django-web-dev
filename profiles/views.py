from django.views.generic.edit import CreateView

from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create-profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
