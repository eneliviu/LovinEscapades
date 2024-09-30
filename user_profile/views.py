from django.shortcuts import (render, redirect,
                              get_object_or_404, reverse)
from django.contrib import messages
from django.http import HttpResponseRedirect
from trip.models import Trip
from .models import Profile
from .filters import TripFilter


# Create your views here.
def user_profile(request):
    ''' 
    User profile page
    '''
    trip_filter = TripFilter(request.GET,
                             queryset=Trip.objects.all())
    
    context = {
        'trip_filter_form': trip_filter.form,
        'trips': trip_filter.qs,  # filter queryset
    }
    
    return render(request, 'user_profile/user_profile.html', context)
