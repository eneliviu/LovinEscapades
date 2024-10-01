from django.shortcuts import (render, redirect,
                              get_object_or_404, reverse)
from django.views import generic
from django.contrib.auth.decorators import login_required
# from django.core import serializers
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import (Trip, Comment, Note, Image)
from .forms import AddTripForm, TripSelectionForm


def landing_page(request):
    '''
    View for Landing page
    '''

    # Serialization require a list of objects:
    trips = list(Trip.objects.filter(shared='Yes').values())

    return render(request,
                  'trip/landing_page.html',
                  {'trips': trips})
            

def _trip_stats(trips):
    """
    Calculate trip statistics
    """
    comments_count = 0
    images_count = 0
    if trips:
        for trip in trips:
            comments_count += trip.comments.all().count()
            images_count += trip.images.all().count()
    return comments_count, images_count


def handle_get_request(request):
    trips = Trip.objects.filter(user=request.user).\
        prefetch_related('images', 'comments')
    comments_count, images_count = _trip_stats(trips)
    add_trip_form = AddTripForm()
    context = {
        'trips': trips,
        'comments_count': comments_count,
        'images_count': images_count,
        'add_trip_form': add_trip_form,
    }
    return render(request, "trip/user_page.html", context)


def handle_post_request(request):
    add_trip_form = AddTripForm(request.POST)
    
    if add_trip_form.is_valid():
        trip_form = add_trip_form.save(commit=False)
        trip_form.user = request.user
        trip_form.save()  # Save the trip instance
        
        messages.add_message(
            request,
            messages.SUCCESS,
            f'New trip to {trip_form.place}, {trip_form.country} added'
        )

        # Reload trips and recalculate stats after saving:
        trips = Trip.objects.filter(user=request.user).\
            prefetch_related('images', 'comments')
        comments_count, images_count = _trip_stats(trips)
        # context = {'trips': trips,
        #            'comments_count': comments_count,
        #            'images_count': images_count,
        #            'add_trip_form': AddTripForm(),
        #            }
        # Redirect to avoid re-posting the form on refresh
        return redirect('user')
        # return render(
        #     request,
        #     "trip/user_page.html",
        #     context)
    else:
        messages.add_message(
            request,
            messages.ERROR,
            add_trip_form.errors.as_data())
        return redirect('user')


def user_page(request):
    """
    View for Dashboard
    """
    if request.method == 'GET':
        return handle_get_request(request)
    elif request.method == 'POST':
        return handle_post_request(request)


def trip_filters(request):
    trips = Trip.objects.filter(user=request.user)
    form = TripSelectionForm()
    
    if request.method == 'POST':
        form = TripSelectionForm(request.POST)
        if form.is_valid():
            trip_status = form.cleaned_data['trip_status']
            trip_category = form.cleaned_data['trip_category']
            
            if trip_status:
                trips = trips.filter(trip_status=trip_status)
            if trip_category:
                trips = trips.filter(trip_category=trip_category)
    context = {
        'form': form,
        'trips': trips,
    }

    return render(request,
                  'trip/user_profile.html',
                  context)
   

# def user_registration(request):
#     ''' 
#     Redirect user after registration
#     '''
#     return render(request, 'trip/user_profile.html', {})


def gallery(request):
    ''' 
    Redirect user after registration
    '''
    return render(request, 'trip/shared_gallery.html', {})


def contact(request):
    ''' 
    Redirect user after registration
    '''
    
    return render(request, 'trip/contact_us.html', {})




# def custom_404_view(request, exception):
#     ''' 
#     Render 404 Error page
#     '''
#     return render(request, '404.html', {}, status=404)