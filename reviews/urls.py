from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.ReviewView.as_view(), name='review'),
    path('thank-you', view=views.ThankYouView.as_view(), name='thank-you'),
    path('reviews', view=views.ReviewListView.as_view(), name='review-list'),
    path('reviews/favorite', view=views.AddFavoriteView.as_view(), name='favorite-view'),
    path('reviews/<int:pk>', view=views.SingleReviewView.as_view(), name='single-review'),
]
