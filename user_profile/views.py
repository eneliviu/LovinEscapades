from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404)
from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from allauth.account.forms import SignupForm
from .models import Testimonial
from .forms import TestimonialForm


# Create your views here.

def handle_get_request(request):
    posts = Testimonial.objects.filter(user=request.user)
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


def handle_post_request(request):
    _add_posts_form(request)
    return redirect('profile')


@login_required
def user_profile(request):
    """
    View for Dashboard
    """
    if request.method == 'GET':
        return handle_get_request(request)
    elif request.method == 'POST':
        return handle_post_request(request)



# def user_profile(request):
#     '''
#     User profile page
#     '''

#     posts = Testimonial.objects.filter(user=request.user)
#     return render(
#                 request,
#                 'user_profile/user_profile.html',
#                 context={
#                     'testimonial_form': TestimonialForm(),
#                     'posts': posts
#                     }
#             )


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
            'The record cannot be deleted.'
        )
    return redirect('profile')


def update_profile(request):
    # if request.user.is_authenticated:
    # current_user = User.objects.get(id=request.user.id)
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = SignupForm()
    
    return render(
        request,
        'user_profile/update_user_profile.html',
        {
            'form': form,
        }
    )    
    

# @login_required
# def user_posts(request):
#     posts = Testimonial.objects.all()
#     return render(
#         request,
#         'user_profile/user_profile.html',
#         context={
#             'posts': posts,
#         }

#     )

