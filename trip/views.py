from django.shortcuts import (render, redirect,
                              get_object_or_404, reverse)
from django.views import generic
from django.contrib.auth.decorators import login_required
# from django.core import serializers
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import (Trip, Comment, Note, Image)
from .forms import AddTripForm
from .filters import TripFilter
from user_profile.models import Testimonial


def landing_page(request):
    '''
    View for Landing page
    '''

    # Serialization require a list of objects:
    trips = list(Trip.objects.filter(shared='Yes').
                 order_by('-created_on').values())
    # Fetch testimonials from the database
    testimonials = Testimonial.objects.all()

    trip_filter = TripFilter(request.GET,
                             queryset=Trip.objects.filter(shared='Yes'))

    if trip_filter.qs.exists():
        trips = list(trip_filter.qs.values())
        context = {'trips': trips,
                   'testimonials': testimonials,
                   'trip_filter_form': trip_filter.form,
                   }
    else:
        messages.add_message(
                request,
                messages.ERROR,
                'No matches were found'
            )
        trip_filter = TripFilter(request.GET)
        context = {'trips': trips,
                   'testimonials': testimonials,
                   'trip_filter_form': trip_filter.form,
                   }

    return render(request,
                  'trip/landing_page.html',
                  context=context,
                  )


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


@login_required
def handle_get_request(request):
    trips = Trip.objects.filter(user=request.user).\
            prefetch_related('images', 'comments')
    comments_count, images_count = _trip_stats(trips)
    user = request.user
    print(user)

    testimonials_count = user.testimonials.count()
    add_trip_form = AddTripForm()
    
    # Pagination:
    # https://djangocentral.com/adding-pagination-with-django/#adding-pagination-using-function-based-views
    # 3 trips in each page
    paginator = Paginator(trips, 6)
    page = request.GET.get('page')
    try:
        trip_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        trip_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        trip_list = paginator.page(paginator.num_pages)    
    
    context = {
        'page': page,
        'trips': trip_list,
        'comments_count': comments_count,
        'testimonials_count': testimonials_count,
        'images_count': images_count,
        'add_trip_form': add_trip_form,
    }
    return render(request, "trip/user_page.html", context)


@login_required
def handle_post_request(request):
    add_trip_form = AddTripForm(request.POST, 
                                user=request.user)
    
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
        return redirect('user')
    else:
        cleaned_errors = []
        for field, errors in add_trip_form.errors.items():
            for error in errors:
                if field == '__all__':
                    cleaned_errors.append(error)
                else:
                    cleaned_errors.append(f'{field.replace("_", " ").
                                          capitalize()}: {error}')
        
        messages.add_message(
            request,
            messages.ERROR,
            *cleaned_errors)  # Unpack the error list
        return redirect('user')


def user_page(request):
    """
    View for Dashboard
    """
    if request.method == 'GET':
        return handle_get_request(request)
    elif request.method == 'POST':
        return handle_post_request(request)


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


def trip_edit(request, trip_id):
    """
    Display an individual trip for edit.

    **Context**

    ``trip``
        An instance of :model:`trip.Trip`.
    ``note``
        A note related to the trip.
    ``note_form``
        An instance of :form:`trip.NoteForm`
    """

    if request.method == "POST":

        queryset = Trip.objects.filter(user=request.user)
        post = get_object_or_404(queryset)
        note = get_object_or_404(Comment, pk=trip_id)
        note_form = NoteForm(data=request.POST, instance=note)

        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.post = post
            note.approved = False
            note.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Trip Note Updated!')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating trip note!')

    return HttpResponseRedirect(reverse('post_detail'))


def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)
    if trip.user == request.user:
        trip.delete()
        messages.success(request, 'Trip deleted successfully.')
        return redirect('user')
    return HttpResponseRedirect(reverse('user'))


# def custom_404_view(request, exception):
#     ''' 
#     Render 404 Error page
#     '''
#     return render(request, '404.html', {}, status=404)
