from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.CreateProfileView.as_view(), name="create-profile"),
]
