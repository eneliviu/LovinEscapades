from django.urls import path
from . import views as trip_views


# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path(
        '',
        trip_views.landing_page,
        name='home'
    ),
    path(
        'user_page/',
        trip_views.user_page,
        name='user'
    ),
    # path(
    #     'gallery/',
    #     trip_views.gallery,
    #     name='shared_gallery'
    # ),
    path(
        'delete_trip/<int:trip_id>',
        trip_views.delete_trip,
        name='delete_trip'
    ),
    path(
        'user_page/edit/<int:trip_id>',
        trip_views.edit_trip_page,
        name='edit_page'
    ),
    path(
        'user_page/details/<int:trip_id>',
        trip_views.trip_details_page,
        name='trip_details'
    ),
    path(
        'delete_photo/<int:photo_id>',
        trip_views.delete_photo,
        name='delete_photo'
    ),

    # path('', trip_views.custom_404_view, name='404_page'), <str:username>

]
