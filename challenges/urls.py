from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>', view=views.monthly_challenge_by_number, name="monthly_challenge_by_number"),
    path('<str:month>', view=views.monthly_challenge, name="monthly_challenges"),
]
