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
@login_required
def user_profile(request):
    '''
    User profile page
    '''
    posts = Testimonial.objects.all()
    
    if request.method == 'GET':
        form = TestimonialForm()
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            form = TestimonialForm()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Testimonial submitted succesfully and waiting for approval'
            )
        else:
            form = TestimonialForm()

    return render(
                request,
                'user_profile/user_profile.html',
                context={
                    'testimonial_form': form,
                    'posts': posts
                    }
            )




@login_required
def user_posts(request):
    posts = Testimonial.objects.all()
    return render(
        request,
        'user_profile/user_profile.html',
        context={
            'posts': posts,
        }

    )


# ensure that only logged-in users can submit testimonials
@login_required
def submit_testimonial(request):
    posts = Testimonial.objects.all()
    if request.method == 'GET':
        form = TestimonialForm()
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            form = TestimonialForm()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Testimonial submitted succesfully and waiting for approval'
            )
        else:
            form = TestimonialForm()

    return render(
                request,
                'user_profile/user_profile.html',
                context={
                    'testimonial_form': form,
                    'posts': posts
                    }
            )


@login_required
def delete_post(request, post_id):
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
    
    # return render(
    #     request,
    #     'user_profile/update_user_profile.html',
    #     {}
    # )
    # else:
    #     messages.add_message(
    #             request,
    #             messages.ERROR,
    #             'You must be logged in'
    #         )
    #     return redirect('profile')
