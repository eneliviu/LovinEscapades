from django import forms
from django.contrib.auth.models import User
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['author_name', 'user_info', 'body']

    def clean_text(self):
        body = self.cleaned_data.get('body')
        if len(body) < 20:
            raise forms.ValidationError("The testimonial text must\
                                         be at least 20 characters long.")
        return body

# "This platform made my trip to Europe unforgettable!"
# Travel Enthusiast

# "Sharing my travel notes has never been easier!"
# Travel Blogger

# "An essential tool for every traveler!"
# Adventurer


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
