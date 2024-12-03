from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create-profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user-profiles.html"
    context_object_name = "profiles"