from django.urls import path
from . import views as user_profile_views

# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path(
        '',
        user_profile_views.user_profile,
        name='profile'
    ),
    path(
        'delete_post/<int:post_id>/',
        user_profile_views.delete_post,
        name='delete_testimonial'
    ),
    path(
        'profile/update/',
        user_profile_views.update_profile,
        name='update_user_profile'),
]
