from django.urls import path
from . import views

urlpatterns = [
    path('january', view=views.january, name="january"),
    path('february', view=views.february, name="february"),
    path('march', view=views.march, name="march"),
]