"""
URL configuration for lovinescapades project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


# it is best not to give your URLs the same name
# as your view function or vice-versa.
# Look in app URL file for any trip urlpatterns.
urlpatterns = [
    path('admin', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dashboard/",
         include('user_profile.urls'),
         name='profile'),
    path("dashboard/",
         include('user_profile.urls'),
         name='update_profile'),
    path("", include('trip.urls'), name='trip'),  
    path("", include('trip.urls'), name='gallery'),
    path("", include('trip.urls'), name='contact'),       
]
