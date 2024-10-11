from django.urls import path
from . import views as contact_views

# it is best not to give your URLs the same name
# as your view function or vice-versa.

urlpatterns = [
    path(
        '',
        contact_views.contact_us,
        name='contact'
    ),
]
