from django.urls import path
from . import views as gallery_views


# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path(
        '',
        gallery_views.gallery,
        name='shared_gallery'
    ),
]
