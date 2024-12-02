from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
# from .models import Review

# Create your views here.

def review(request):    
    if request.method == "POST":
        # # in case we want to update a existing data 
        # existing_data = Review.objects.get(pk=1)   # fetching the data from the database
        # form = ReviewForm(request.POST, instance=existing_data)  # this line of code takes the data from the currently entered form and updates that into the existing data
        form = ReviewForm(request.POST,)  # validating the user entered form

        if form.is_valid():
            print(form.cleaned_data)
            # user_review = Review(user_name=form.cleaned_data['user_name'],
            #                      review_text=form.cleaned_data['review_text'],
            #                      rating=form.cleaned_data['rating'])
            # user_review.save()

            # since we are using modelform now we can directly call save method to save data into database
            form.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    
    # if the form is not valid, django will attach some meaningful error messages with the form and if the request is GET then a fresh new form will be rendered
    return render(request=request, template_name="reviews/review.html", context={"form": form})


def thank_you(request):
    return render(request=request, template_name="reviews/thank-you.html")
