from django.shortcuts import render, redirect
from django.views import generic
from django.core import serializers
from .models import (Trip, Comment, Note, Image)
from .forms import AddTripForm


def user_page(request):
    '''
    View for Dashboard
    '''
    def _trip_stats(trips):
        '''
        Calculate trip statistics
        '''
        comments_count = 0
        images_count = 0
        if trips:
            for trip in trips:
                comments_count += trip.comments.all().count()
                images_count += trip.images.all().count()
        return comments_count, images_count

    add_trip_form = AddTripForm(request.POST or None)
  
    if request.method == 'GET':
        trips = Trip.objects.filter(user=request.user).prefetch_related('images', 'comments')
        comments_count, images_count = _trip_stats(trips)
       
    if request.method == 'POST':
        if add_trip_form.is_valid():
            trip = add_trip_form.save(commit=False)
            trip.user = request.user
            add_trip_form.save()
            print('Trip saved')
            
            # Reload trips and recalculate stats after saving:
            add_trip_form = AddTripForm()
            trips = Trip.objects.filter(user=request.user).prefetch_related('images', 'comments')
            comments_count, images_count = _trip_stats(trips)

            # Redirect to avoid re-posting the form on refresh
            return redirect('user')

            # messages.add_message(
            #     request,
            #     messages.SUCCESS,
            #     'Trip info succesfully added'
            # )
            # trip = list(Trip.objects.values())
            # return render(request,
            #               "trip/user_page.html",
            #               {})
        else:
            # print(add_trip_form.errors.as_data())
            # messages.add_message(
            #     request,
            #     messages.ERROR,
            #     form.errors.as_data()
            # )
            add_trip_form = AddTripForm()

    context = {
        'trips': trips,
        'comments_count': comments_count,
        'images_count': images_count,
        'add_trip_form': add_trip_form,
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
    print(request.path)
    return render(request, 'trip/user_profile.html', {})


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


def landing_page(request):
    '''
    View for Landing page
    '''

    if request.method == 'GET':
        add_trip_form = AddTripForm(request.GET)
        if Trip.objects.all().last() is None:  # Handle no trip records
            context = {'add_trip_form': add_trip_form}
        else:  # Get all the trips  
            # List the trip values to serialize in Leaflet
            trips = list(Trip.objects.values().filter(shared=True))
            # print(trips)
            context = {'add_trip_form': add_trip_form,
                       'trips': trips,
                       }
        return render(request,
                      'trip/landing_page.html',
                      context=context)

    if request.method == 'POST':
        add_trip_form = AddTripForm(request.POST or None)
        if add_trip_form.is_valid():
            trip = add_trip_form.save(commit=False)
            trip.user = request.user
            add_trip_form.save()
            # messages.add_message(
            #     request,
            #     messages.SUCCESS,
            #     'Trip info succesfully added'
            # )
            # trip = list(Trip.objects.values())
            return redirect('trip/landing_page.html')
        else:
            # print(add_trip_form.errors.as_data())
            # messages.add_message(
            #     request,
            #     messages.ERROR,
            #     form.errors.as_data()
            # )
            add_trip_form = AddTripForm()
            return render(request, 
                          'trip/landing_page.html',
                          {'add_trip_form': add_trip_form})





# def custom_404_view(request, exception):
#     ''' 
#     Render 404 Error page
#     '''
#     return render(request, '404.html', {}, status=404)