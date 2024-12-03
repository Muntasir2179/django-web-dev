from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm

# Create your views here.

def store_file(file):
    with open(f"temp/{file.name}", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request=request, template_name="profiles/create-profile.html", context={"form": form})
    
    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            print(request.FILES['image'].name)    # request has FILES attribute which contains all the uploaded files as a dictionary
            store_file(request.FILES['image'])
            return HttpResponseRedirect("/profiles")
        return render(request=request, template_name="profiles/create-profile.html", context={"form": submitted_form})
