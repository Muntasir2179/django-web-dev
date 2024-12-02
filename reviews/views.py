from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

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


# class ThankYouView(View):
#     def get(self, request):
#         return render(request=request, template_name="reviews/thank-you.html")


class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for submitting the feedback."
        return context


class ReviewListView(TemplateView):
    template_name = "reviews/reviews-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context