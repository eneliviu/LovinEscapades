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

def handle_get_request_profile_page(request):
    posts = Testimonial.objects.filter(user=request.user).order_by('-created_at')
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
    Handle form for posting new posts
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


def handle_post_request_add_post(request):
    _add_posts_form(request)
    return redirect('profile')


@login_required
def user_profile(request):
    """
    View for User Profile
    https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django
    """
    if request.method == 'GET':
        return handle_get_request_profile_page(request)
    elif request.method == 'POST':
        if request.POST.get("form_type") == 'addTestimonialForm':
            return handle_post_request_add_post(request)


@login_required
def delete_post(request, post_id):
    '''
    same as in trip,views - make one function in utils.py
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
