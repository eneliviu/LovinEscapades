from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from user_profile.models import Testimonial
from .models import Trip, Image
from .forms import AddTripForm, EditTripForm, UploadImageForm
from .filters import TripFilter


@login_required
def landing_page(request):
    '''
    View for Landing page
    '''

    # Serialization require a list of objects:
    trips = list(Trip.objects.filter(shared='Yes').
                 order_by('-created_on').values())
    # Fetch testimonials from the database
    testimonials = Testimonial.objects.filter(approved=True)
    trip_filter = TripFilter(request.GET,
                             queryset=Trip.objects.filter(shared='Yes'))
    if trip_filter.qs.exists():
        trips = list(trip_filter.qs.values())
        context = {
            'trips': trips,
            'testimonials': testimonials,
            'trip_filter_form': trip_filter.form,
        }
    else:
        if len(trips) == 0:
            messages.add_message(
                request,
                messages.ERROR,
                'No trips are posted'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'No matches were found'
            )
        trip_filter = TripFilter()
        context = {
            'trips': trips,
            'testimonials': testimonials,
            'trip_filter_form': trip_filter.form,
        }

    return render(
        request,
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
def _add_trip_form(request):
    '''
    Handle form for creating new trips
    '''
    add_trip_form = AddTripForm(request.POST, user=request.user)
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
            prefetch_related('images')
        comments_count, images_count = _trip_stats(trips)
    else:
        cleaned_errors = []
        for field, errors in add_trip_form.errors.items():
            print(*errors)
            for error in errors:
                print(error)
                if field == '__all__':
                    cleaned_errors.append(error)
                else:
                    cleaned_errors.append(f'{field.replace("_", " ").
                                          capitalize()}: {error}')
        messages.add_message(
                request,
                messages.ERROR,
                *cleaned_errors)  # Unpack the error list


@login_required
def delete_trip(request, trip_id):
    qs = Trip.objects.filter(user=request.user)
    trip = get_object_or_404(qs, id=trip_id)
    if trip:
        trip.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Trip deleted successfully.'
        )
        print(messages)
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Error: The record cannot be deleted.'
        )
    return redirect('user')


@login_required
def handle_get_request_user_page(request):
    '''
    Pagination:
    https://djangocentral.com/adding-pagination-with-django/#adding-pagination-using-function-based-views
    '''
    trips = Trip.objects.filter(user=request.user).prefetch_related('images')
    comments_count, images_count = _trip_stats(trips)
    user = request.user

    testimonials_active = user.testimonials.filter(approved=True).count()
    testimonials_pending = user.testimonials.filter(approved=False).count()
    testimonials_all = testimonials_active + testimonials_pending

    add_trip_form = AddTripForm()
    paginator = Paginator(trips, 6)  # 6 trips in each page
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
        'testimonials_count_active': testimonials_active,
        'testimonials_count_pending': testimonials_pending,
        'testimonials_count_all': testimonials_all,
        'images_count': images_count,
        'add_trip_form': add_trip_form,
    }
    return render(request, "trip/user_page.html", context)


@login_required
def handle_post_request_user_page(request):
    _add_trip_form(request)
    return redirect('user')


def user_page(request):
    """
    View for Dashboard
    """
    if request.method == 'GET':
        return handle_get_request_user_page(request)
    elif request.method == 'POST':
        return handle_post_request_user_page(request)


def custom_404_view(request, exception):
    '''
    Render 404 Error page
    '''
    return render(
        request,
        '404.html',
        {},
        status=404
    )


# ==================================================== #


def gallery(request, trip_id):
    '''
    Redirect user after registration
    '''
    trip = get_object_or_404(Trip, pk=trip_id, user=request.user)
    images = trip.images.all()
    return render(
        request,
        'trip/shared_gallery.html',
        context={
            'images': images,
            'trips': trip,
        }
    )


def contact(request):
    '''
    Redirect user after registration
    '''
    return render(request, 'trip/contact_us.html', {})

# ==================================================== #


def _edit_trip_form(request, trip_id):
    """
    Display an individual trip for edit.
    """
    trip = get_object_or_404(Trip, user=request.user, id=trip_id)
    # Pre-populates form with existing trip data
    form = EditTripForm(request.POST, instance=trip)
    if form.is_valid():
        form.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Trip updated successfully!'
        )
    else:
        cleaned_errors = []
        for field, errors in form.errors.items():
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


def _upload_trip_images(request, trip_id):
    trip = get_object_or_404(Trip, user=request.user, id=trip_id)
    if request.method == 'POST':
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.trip = trip  # Foreign key
            image.save()
            if image.shared:
                msg = 'Image loaded successfully and added to the Gallery!'
            else:
                msg = 'Image loaded successfully!'
            messages.add_message(
                request,
                messages.SUCCESS,
                msg
            )
    else:
        image_form = UploadImageForm()


@login_required
def handle_get_request_edit_trip_page(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)
    trip_form = EditTripForm(instance=trip)
    image_form = UploadImageForm()
    return render(
        request,
        "trip/edit_trip.html",
        context={
            'image_form': image_form,
            'edit_trip_form': trip_form,
        }
    )


@login_required
def handle_post_request_edit_trip(request, trip_id):
    _edit_trip_form(request, trip_id)
    return redirect('edit_page', trip_id=trip_id)  # back to edit page


def handle_post_request_upload_image(request, trip_id):
    _upload_trip_images(request, trip_id)
    return redirect('edit_page', trip_id=trip_id)  # back to edit page


@login_required
def edit_trip_page(request, trip_id):
    """
    View for Dashboard
    https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django
    """
    if request.method == 'GET':
        return handle_get_request_edit_trip_page(request, trip_id)
    elif request.method == 'POST':
        if request.POST.get("form_type") == 'editTripForm':
            return handle_post_request_edit_trip(request, trip_id)
        elif request.POST.get("form_type") == 'uploadImageForm':
            return handle_post_request_upload_image(request, trip_id)


@login_required
def _trip_details(request, trip_id):
    trip = get_object_or_404(
            Trip,
            user=request.user,
            pk=trip_id
        )
    images = trip.images.all()
    return render(
            request,
            "trip/trip_details.html",
            context={
                'selected_trip': trip,
                'trip_images':  images,
            }
        )


@login_required
def trip_details_page(request, trip_id):
    trip = get_object_or_404(
            Trip,
            user=request.user,
            id=trip_id
        )
    images = trip.images.all()
    return render(
            request,
            "trip/trip_details.html",
            context={
                'selected_trip': trip,
                'trip_images':  images,
            }
        )


@login_required
def delete_photo(request, photo_id):
    image = Image.objects.filter(id=photo_id)
    print(image.values())
    if image:
        image.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Photo deleted successfully.'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Error: The record cannot be deleted.'
        )
    return redirect('user')
