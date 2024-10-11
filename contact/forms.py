from .models import ContactUs
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(
                attrs={
                        'minlength': '2',
                        'maxlength': '200'
                        }
                ),
            'email': forms.EmailInput(
                attrs={
                        'maxlength': '254'
                    }
                ),  # Standard max length for emails
            'message': forms.Textarea(attrs={
                'minlength': '50',
                'maxlength': '500'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # Mark all fields as required:
        for field in self.fields.values():
            field.required = True

    def clean_message(self):
        message = self.cleaned_data.get('message').strip()
        if len(message) < 50:
            raise forms.ValidationError("Message must be at least 50\
                characters long.")
        if len(message) > 500:
            raise forms.ValidationError("Message must be at most 500\
                characters long.")
        return message

    def clean_name(self):
        name = self.cleaned_data.get('name').strip()
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2\
                characters long.")
        return name
