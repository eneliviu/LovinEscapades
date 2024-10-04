from django.urls import path
from . import views as trip_views


# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path(
        'user/',
        trip_views.user_page,
        name='user'
    ),
    path(
        'gallery/',
        trip_views.gallery,
        name='gallery'
    ),
    path(
        'contact/',
        trip_views.contact,
        name='contact'
    ),
    path(
        'delete_trip/<int:trip_id>',
        trip_views.delete_trip,
        name='delete_trip'
    ),
    path(
        'edit_trip/<int:pk>',
        trip_views.edit_trip,
        name='edit_trip'
    ),
    path(
        '',
        trip_views.landing_page,
        name='home'
    ),
    # path('', trip_views.custom_404_view, name='404_page'), <str:username>
]