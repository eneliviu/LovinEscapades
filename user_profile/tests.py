from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Testimonial
from .forms import TestimonialForm



# Create your tests here.

    def setUp(self):
        # Create a user and log them in for testing purposes
        self.user = User.objects.create_user(username='testuser', password='secure123')
        self.client = Client()
        self.client.login(username='testuser', password='secure123')
        
        # Prepare the URL and form data
        self.url = reverse('submit_testimonial')  # Ensure that your URL name is correct
        self.valid_data = {
            'body': 'This is a test testimonial.',
        }
        self.invalid_data = {
            'body': '',  # Assuming 'body' is required
        }

    def test_submit_testimonial_get(self):
        response = self.client.get(self.url)
        
        # Ensure the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Assert the correct template was used
        self.assertTemplateUsed(response, 'user_profile/user_profile.html')
        
        # Ensure the form is in context
        self.assertIn('testimonial_form', response.context)
        self.assertIsInstance(response.context['testimonial_form'], TestimonialForm)
        
        # Check that 'posts' is in context and contains all testimonials
        self.assertIn('posts', response.context)
        self.assertQuerysetEqual(
            response.context['posts'],
            Testimonial.objects.all(),
            transform=lambda x: x
        )

    def test_submit_testimonial_post_valid(self):
        response = self.client.post(self.url, data=self.valid_data)
        
        # Check redirection after successful post (if you do so) or re-render
        self.assertEqual(response.status_code, 200)
        
        # Check that a new Testimonial object was created
        self.assertEqual(Testimonial.objects.count(), 1)
        self.assertEqual(Testimonial.objects.first().body, 'This is a test testimonial.')
        self.assertEqual(Testimonial.objects.first().user, self.user)
        
        # Check if success message is present
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Testimonial submitted succesfully and waiting for approval')

    def test_submit_testimonial_post_invalid(self):
        response = self.client.post(self.url, data=self.invalid_data)
        
        # Ensure the view re-renders with status code 200
        self.assertEqual(response.status_code, 200)
        
        # Ensure the form is still invalid
        self.assertTrue(response.context['testimonial_form'].errors)
        
        # Ensure no Testimonial was created
        self.assertEqual(Testimonial.objects.count(), 0)