from django.urls import path
from . import views as trip_views


# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path('', trip_views.landing_page, name='home'),
    path('dashboard/', trip_views.user_page, name='user'),
    # path('', trip_views.custom_404_view, name='404_page'), <str:username>
    path('dashboard/user_profile', trip_views.user_profile, name='profile'),
]
