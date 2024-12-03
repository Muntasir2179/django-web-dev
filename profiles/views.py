from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request=request, template_name="profiles/create-profile.html", context={"form": form})
    
    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)   # validating user submitted form, Note that data and files argument are separated

        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])  # request has FILES attribute which contains all the uploaded files as a dictionary, key will be the form field variable name
            profile.save()    # saving data into database and storing files into the designated directory and keeping the files path in the database
            return HttpResponseRedirect("/profiles")
        return render(request=request, template_name="profiles/create-profile.html", context={"form": submitted_form})
