from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(FormView):
    form_class = ReviewForm   # modelform/form class to be used
    template_name = "reviews/review.html"   # template to render
    success_url = "/thank-you"  # url to redirect when successful form submission

    def form_valid(self, form):   # what to do with form data
        form.save()
        return super().form_valid(form)


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


class SingleReviewView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review
    context_object_name = "review"

