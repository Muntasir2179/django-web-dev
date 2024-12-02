from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name",
#                                 max_length=100,
#                                 error_messages={
#                                     "required": "Your name must not be empty",
#                                     "max_length": "Please enter a shorter name"
#                                 })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea(), max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # We can specify a python list of model attributes that we want to include into the form
        # exclude = ["user_name"]   # this attribute is for defining which model fields we dont want to include into the form

        # this attribute is used for defining the labels for each model fields
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Rating"
        }

        # this attribute is used for defining the error message for each model fields
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name"
            }
        }