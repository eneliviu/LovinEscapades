from django.shortcuts import render
from django.views import generic
from .models import (Trip, Activity, Comment, Note, Image)

# Create your views here.


# Create your views here.
# def landing_page(request):
#     '''
#     View for Landing page
#     '''
#     return render(request, "trip/landing_page.html")



def landing_page(request):
    print(request)
    
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
        
        trips = list(Trip.objects.values())
        print(trips)
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