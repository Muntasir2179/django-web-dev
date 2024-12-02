from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.ReviewView.as_view(), name='review'),
    path('thank-you', view=views.ThankYouView.as_view(), name='thank-you'),
    path('reviews', view=views.ReviewListView.as_view(), name='review-list'),
]
