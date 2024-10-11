from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def contact_us(request):
    '''
    Renders the most recent information on the website
    and allows user inqueries.

    **Context**
    ``contact_form``
        An instance of :form:`contact.ContactForm`
    **Template**
        :template:`contact/about.html`
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
