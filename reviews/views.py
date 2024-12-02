from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request=request, template_name="reviews/review.html", context={"form": form})


    def post(self, request):
        form = ReviewForm(request.POST)  # validating the user entered form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request=request, template_name="reviews/review.html", context={"form": form})


def thank_you(request):
    return render(request=request, template_name="reviews/thank-you.html")
