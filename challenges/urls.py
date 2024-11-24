from django.urls import path
from . import views

urlpatterns = [
    path('<month>', view=views.monthly_challenge, name="monthly_challenges"),
]
