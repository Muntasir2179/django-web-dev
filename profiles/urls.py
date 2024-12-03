from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.CreateProfileView.as_view(), name="create-profile"),
    path('list', view=views.ProfilesView.as_view(), name='user-profiles'),
]
