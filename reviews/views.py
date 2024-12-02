from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
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


class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for submitting the feedback."
        return context


class ReviewListView(ListView):
    template_name = "reviews/reviews-list.html"   # template to render
    model = Review   # model class to use for fetching data
    context_object_name = "reviews"    # name of the context variable default name is "object_list"

    # # suppose we want to fetch data conditionally
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review
    context_object_name = "review"

