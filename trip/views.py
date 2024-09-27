from django.shortcuts import render
from django.views import generic
from django.core import serializers
from .models import (Trip, Activity, Comment, Note, Image)
from .forms import AddTripForm


def user_page(request):
    '''
    View for Dashboard
    '''
    # trips = Trip.objects.values().filter(user=request.user).prefetch_related('images')
    trips = Trip.objects.filter(user=request.user).prefetch_related('images')
    comments_count = 0
    images_count = 0
    if trips:
        for trip in trips:
            comments_count += trip.comments.all().count()
            images_count += trip.images.all().count()

    context = {
        'trips': trips,
        'comments_count': comments_count,
        'images_count': images_count
    }

    return render(request, "trip/user_page.html", context)


def user_registration(request):
    ''' 
    Redirect user after registration
    '''
    return render(request, 'trip/user_page.html', {})


def user_logout(request):
    pass

def user_profile(request):
    ''' 
    User profile page
    '''
    return render(request, 'trip/user_profile.html', {})


def gallery(request):
    ''' 
    Redirect user after registration
    '''
    print(request.path)
    return render(request, 'trip/shared_gallery.html', {})


def contact(request):
    ''' 
    Redirect user after registration
    '''
    print(request.path)
    return render(request, 'trip/contact_us.html', {})




def landing_page(request):
    '''
    View for Landing page
    ''' 
    if request.method == 'GET':
        # Handle no trip data:
        if Trip.objects.all().last() is None:
            # form = TripForm()
            # context = {'form': form}
        # else:
            # Get all the trips:
            
            # List the trip values to serialize in Leaflet
            trips = list(Trip.objects.values())
            # form = TripForm()
            context = {# 'form': form,
                       'trips': trips}
        
        trips = list(Trip.objects.values().
                     filter(shared=True))
        # print(trips)
        return render(request, 
                      'trip/landing_page.html',
                      context={'trips': trips})

    # if request.method == 'POST':
    #     form = TripForm(request.POST)
    #     if form.is_valid():
    #         trip = form.save(commit=False)
    #         trip.tourist = request.user
    #         print(trip)
    #         form.save()
    #         messages.add_message(
    #             request,
    #             messages.SUCCESS,
    #             'Trip info succesfully added'
    #         )
    #         trip = list(Trip.objects.values())
    #         redirect('leaflet_map.html')
    #     else:
    #         print(form.errors.as_data())
    #         messages.add_message(
    #             request,
    #             messages.ERROR,
    #             form.errors.as_data()
    #         )
    
    # form = TripForm()
    # context = {'form': form,
    #            'trips': trips}
    
    return render(request, 
                  'trip/landing_page.html',
                  context={'trips': trips})


# def custom_404_view(request, exception):
#     ''' 
#     Render 404 Error page
#     '''
#     return render(request, '404.html', {}, status=404)