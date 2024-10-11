from django import forms
from django.contrib.auth.models import User
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    '''
    # "This platform made my trip to Europe unforgettable!"
    # Travel Enthusiast

    # "Sharing my travel notes has never been easier!"
    # Travel Blogger

    # "An essential tool for every traveler!"
    # Adventurer

    '''
    class Meta:
        model = Testimonial
        fields = ['author_name', 'user_info', 'body']
        widgets = {
            'author_name': forms.TextInput(
                attrs={
                        'minlength': '2',
                        'maxlength': '50'
                        }
                ),
            'user_info': forms.TextInput(
                attrs={
                        'minlength': '2',
                        'maxlength': '50'
                    }
                ),  # Standard max length for emails
            'body': forms.Textarea(attrs={
                'minlength': '20',
                'maxlength': '100'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        # Mark all fields as required:
        for field in self.fields.values():
            field.required = True

    def clean_text(self):
        body = self.cleaned_data.get('body').strip()
        if len(body) < 20:
            raise forms.ValidationError("The testimonial text must\
                                        be at least 20 characters long.")
        if len(body) > 100:
            raise forms.ValidationError("The testimonial text must\
                                        be at most 100 characters long.")
        return body

    def clean_name(self):
        author_name = self.cleaned_data.get('author_name').strip()
        if len(author_name) < 2:
            raise forms.ValidationError("Name must be at least 2\
                characters long.")
        return author_name

    def clean_info(self):
        user_info = self.cleaned_data.get('user_info').strip()
        if len(user_info) < 2:
            raise forms.ValidationError("User info must be at least 2\
                characters long.")
        return user_info


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                        'minlength': '2',
                        'maxlength': '200'
                        }
                ),
            'first_name': forms.TextInput(
                attrs={
                        'minlength': '2',
                        'maxlength': '50'
                        }
                ),
            'last_name': forms.TextInput(
                attrs={
                        'minlength': '2',
                        'maxlength': '50'
                    }
                ),
            'email': forms.EmailInput(
                attrs={  # Standard max length for emails
                        'maxlength': '254'
                    }
                ),
        }

    # make the 'email' field obligatory
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    # def clean_first_name(self):
    #     name = self.cleaned_data.get('first_name').strip()
    #     if len(name) < 2:
    #         raise forms.ValidationError("Name must be at least 2\
    #             characters long.")
    #     return name

    # def clean_second_name(self):
    #     name = self.cleaned_data.get('second_name').strip()
    #     if len(name) < 2:
    #         raise forms.ValidationError("Name must be at least 2\
    #             characters long.")
    #     return name
