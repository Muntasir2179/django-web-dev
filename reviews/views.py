from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    """Use of this CreateView completely erases the use of forms. We can create and validate form using model class and also save the data into the database."""
    model = Review    # model class to be used for creating form
    fields = '__all__'   # list of the fields that are used in form
    # form_class = ReviewForm   # modelform/form class to be used
    template_name = "reviews/review.html"   # template to render
    success_url = "/thank-you"  # url to redirect when successful form submission


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object    # we can access the loaded object by using self.object
        request = self.request
        # favorite_id = request.session['favorite_review']   # this way of accessing session data can show a error if the data does not exists in the session
        favorite_id = request.session.get('favorite_review')  # but in this way it will not show any error if the data is not exists in the session
        # primitive data types like int, float, double are stored in session as string thats why we have to convert id that we get from model object to string for fair comparison.
        # we can do opposite as well.
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)
