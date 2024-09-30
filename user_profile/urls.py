from django.urls import path
from . import views as user_profile_views

# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path('', 
         user_profile_views.user_profile,
         name='profile'),
]
