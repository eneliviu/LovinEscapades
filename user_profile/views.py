from django.shortcuts import (render, redirect,
                              get_object_or_404, reverse)
from django.contrib import messages
# from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from trip.models import Trip
from .models import Profile, Testimonial
from .forms import TestimonialForm


from .filters import TripFilter


# Create your views here.
def user_profile(request):
    '''
    User profile page
    '''
    trip_filter = TripFilter(request.GET,
                             queryset=Trip.objects.filter(user=request.user))

    if trip_filter.qs.exists():
        context = {
            'trip_filter_form': trip_filter.form,
            'trips': trip_filter.qs,
        }
    else:
        messages.add_message(
                request,
                messages.ERROR,
                'No matches were found'
            )
        context = {'trip_filter_form': trip_filter.form}

        # return redirect('profile')
    return render(request,
                  'user_profile/user_profile.html',
                  context=context)


def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Testimonial submitted and awaiting approval'
            )
        else:
            form = TestimonialForm()
        
    return render(
                request,
                'user_profile/user_profile.html',
                context={'testimonial_form': form},
                )

@login_required
def update_profile(request):
    # if request.user.is_authenticated:
    # current_user = User.objects.get(id=request.user.id)
    form = SignupForm(request.POST)
    print(form)
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
