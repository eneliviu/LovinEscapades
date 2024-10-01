from django.urls import path
from . import views as trip_views


# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path('dashboard/user',       trip_views.user_page, name='user'),
    path('dashboard/gallery',    trip_views.gallery, name='gallery'),
    path('dashboard/contact_us', trip_views.contact, name='contact'),
    path('',                     trip_views.landing_page, name='home'),
    # path('', trip_views.custom_404_view, name='404_page'), <str:username>
]
