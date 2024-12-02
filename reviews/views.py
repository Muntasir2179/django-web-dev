from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.

def review(request):    
    if request.method == "POST":
        form = ReviewForm(request.POST)  # validating the user entered form

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    
    # if the form is not valid, django will attach some meaningful error messages with the form and if the request is GET then a fresh new form will be rendered
    return render(request=request, template_name="reviews/review.html", context={"form": form})


def thank_you(request):
    return render(request=request, template_name="reviews/thank-you.html")