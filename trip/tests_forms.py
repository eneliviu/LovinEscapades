from django.test import TestCase
from .forms import AddTripForm


# Create your tests here.
class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        add_trip_form = AddTripForm({'description': 'This is a great post'})
        self.assertTrue(add_trip_form.is_valid())
