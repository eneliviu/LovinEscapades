from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def contact_us(request):
    '''
    Processes user inquiries submitted through the contact form, saving the
    information to the database and providing user feedback.

    **Context**
    ``contact_form``
        An instance of :form:`contact.ContactForm`

    **Template**
    :template:`contact/contact_page.html`

    **Functionality**
    - Handles GET requests by returning an empty contact form.
    - Handles POST requests by validating and saving submitted form data.
    - Adds a success message to inform users of successful form submission.
    - Redirects to the contact page upon successful submission.
    '''

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                        request,
                        messages.SUCCESS,  # message tag
                        'Inquiry received! We endeavour to respond\
                            within 2 working days'
                    )
            return redirect('contact')
    else:
        contact_form = ContactForm()

    return render(
        request,
        'contact/contact_page.html',
        context={
            'contact_form': contact_form
        }
    )
