from django.test import TestCase
from .forms import AddTripForm

# Create your tests here.
class TestAddTripForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = AddTripForm({
            'place': '',
            'email': 'test@test.com',
            'country': ''
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
