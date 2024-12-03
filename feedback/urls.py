"""
URL configuration for feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('profiles/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # this adds a static url to the urlpatterns for accessing media files exposed by django


"""
Django by default restricts the access of all the files other that templates and static files. For exposing the media files we have to tell django not to restrict designated
media directories. Only then we can use those files in template.

    1. We have to add MEDIA_URL and MEDIA_ROOT configurations in the settings.py file.
        * MEDIA_URL -> URL path for media files just like URL path we added in urlpatterns list for rendering templates.
        * MEDIA_ROOT -> path of the folder where the files are stored physically. Also used for storing files.
    
    2. We have to add static url in the urlpatterns in the projects urls.py file.
        * We just have to make the connection of MEDIA_URL and MEDIA_ROOT
    
    3. After doing all these we can access media files in the html templates from the designated folder using "url" attribute of a django returned file.

"""