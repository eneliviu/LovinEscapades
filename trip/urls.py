from django.urls import path
from . import views as trip_views


# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path('', trip_views.landing_page, name='home'),
]
