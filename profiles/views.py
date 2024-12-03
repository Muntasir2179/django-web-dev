from django.shortcuts import render
from django.views import View

# Create your views here.

class CreateProfileView(View):
    def get(self, request):
        return render(request=request, template_name="profiles/create-profile.html")
    
    def post(self, request):
        pass