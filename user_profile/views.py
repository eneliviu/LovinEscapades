from django.shortcuts import (render, redirect,
                              get_object_or_404)
from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from allauth.account.forms import SignupForm
from .models import Testimonial
from .forms import TestimonialForm, UpdateProfileForm


# Create your views here.
@login_required
def handle_get_request_profile_page(request):
    '''
    Renders the user profile page with testimonials.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Retrieves all testimonials for the logged-in user,
        ordered by creation date.
    - Initializes a blank testimonial form for user input.
    - Renders the "user_profile.html" template with testimonials and the form.
    '''
    posts = Testimonial.objects.filter(user=request.user)\
        .order_by('-created_at')
    testimonial_form = TestimonialForm()
    context = {
            'testimonial_form': testimonial_form,
            'posts': posts
        }
    return render(
        request,
        "user_profile/user_profile.html",
        context
    )


def _add_posts_form(request):
    '''
    Processes the form submission for adding new testimonials.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Validates and saves a new testimonial associated with the logged-in user.
    - Displays a success message if the form is valid.
    - Collects and displays error messages if the form submission fails.
    '''
    posts_form = TestimonialForm(request.POST)
    if posts_form.is_valid():
        testimonial = posts_form.save(commit=False)
        testimonial.user = request.user
        testimonial.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Testimonial submitted succesfully and waiting for approval'
        )
    else:
        cleaned_errors = []
        for field, errors in posts_form.errors.items():
            for error in errors:
                if field == '__all__':
                    cleaned_errors.append(error)
                else:
                    cleaned_errors.append(f'{field.replace("_", " ").
                                          capitalize()}: {error}')
        messages.add_message(
                request,
                messages.ERROR,
                *cleaned_errors)


@login_required
def handle_post_request_add_post(request):
    '''
    Processes the POST request for adding a new testimonial.
    Redirects to the profile page.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Calls `_add_posts_form` to process the form submission for a new post.
    - Redirects the user to the profile page after form processing.
    '''
    _add_posts_form(request)
    return redirect('profile')


@login_required
def user_profile(request):
    '''
    Manages the display and updates for the user profile page.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Handles GET requests to display the profile page with user testimonials.
    - Processes POST requests to add new testimonials when the appropriate
        form is submitted.
    - Requires the user to be logged in.

    **References**
    - Discussion on handling multiple forms:
    https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django
    '''
    if request.method == 'GET':
        return handle_get_request_profile_page(request)
    elif request.method == 'POST':
        if request.POST.get("form_type") == 'addTestimonialForm':
            return handle_post_request_add_post(request)


@login_required
def delete_post(request, post_id):
    '''
    Deletes a testimonial post for the logged-in user.

    **Parameters**
    - `request`: The HTTP request object.
    - `post_id`: The ID of the testimonial post to be deleted.

    **Functionality**
    - Retrieves and deletes the specified post if it belongs to the user.
    - Displays success or error messages based on the operation result.
    - Redirects the user back to their profile page.

    **Note**
    - Similar to trip deletion, refactor into a shared utility function.
    '''
    qs = Testimonial.objects.filter(user=request.user)
    post = get_object_or_404(qs, id=post_id)
    if post:
        post.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Post deleted successfully.'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'The record could not be deleted.'
        )
    return redirect('profile')


@login_required
def update_profile(request):
    '''
    Updates the profile information of the logged-in user.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Displays the current user profile information in a form for editing.
    - Handles form submission to update the profile.
    - Validates the form data and saves changes if valid.
    - Redirects to the profile page upon successful update.
    - Renders the template for GET requests or invalid submissions.

    **Template**
    - Renders: 'user_profile/edit_user_profile.html'
    '''
    form = UpdateProfileForm(instance=request.user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = UpdateProfileForm(instance=request.user)

    return render(
        request,
        'user_profile/edit_user_profile.html',
        context={'form': form}
    )
