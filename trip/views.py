from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from user_profile.models import Testimonial
from .models import Trip, Image
from .forms import AddTripForm, EditTripForm, UploadImageForm
from .filters import TripFilter


def landing_page(request):
    '''
     Renders the landing page with shared trips and approved testimonials.

    **Context**
    - ``trips``: List of filtered shared :model:`Trip`
    - ``testimonials``: Approved :model:`Testimonial`
    - ``trip_filter_form``: Trip filter form

    **Template**
    :template:`trip/landing_page.html`
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
                messages.SUCCESS,
                'No trips are posted yet!'
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
    Calculates the total number of comments and images across trips.

    :param trips: A list or queryset of :model:`Trip` objects.
    :return: A tuple containing total comment count and image count.
    """
    comments_count = 0
    images_count = 0
    if trips:
        for trip in trips:
            comments_count += trip.comments.all().count()
            images_count += trip.images.all().count()
    return comments_count, images_count


def _add_trip_form(request):
    '''
    Handles the submission and validation of the new trip form.

    :param request: The HTTP request object containing form data.
    :return: Updates user messages with success or error feedback.
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


@login_required
def delete_trip(request, trip_id):
    '''
    Allows an authenticated user to delete their own trip.
    Since it modifies personal data, only authorized users
    should access this functionality.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip to be deleted.

    **Functionality**
    - Deletes the specified trip if it belongs to the user.
    - Adds a success or error message upon completion.
    - Redirects the user to their dashboard.
    '''
    qs = Trip.objects.filter(user=request.user)
    trip = get_object_or_404(qs, id=trip_id)
    if trip:
        trip.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Trip deleted successfully.'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Error: The record cannot be deleted.'
        )
    return redirect('user')


def handle_get_request_user_page(request):
    '''
    Renders the user's trip page with pagination and trip statistics.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Retrieves and paginates the user's trips.
    - Calculates trip statistics including comments and images count.
    - Provides counts of active and pending testimonials.
    - Prepares a form for adding new trips.
    - Renders the "user_page.html" template with the prepared context.

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


def handle_post_request_user_page(request):
    '''
    Processes POST requests for the user's trip page.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Calls the `_add_trip_form` to handle trip form submission.
    - Redirects the user to their trip page after submission.
    '''
    _add_trip_form(request)
    return redirect('user')


@login_required
def user_page(request):
    '''
    This function serves as the user's dashboard, handling both GET
    and POST requests related to a user's personal data.
    It requires the user to be logged in.

    **Parameters**
    - `request`: The HTTP request object.

    **Functionality**
    - Redirects GET requests to handle retrieval and display of user data.
    - Processes POST requests for adding new data.
    - Requires the user to be logged in to access the dashboard.
    '''
    if request.method == 'GET':
        return handle_get_request_user_page(request)
    elif request.method == 'POST':
        return handle_post_request_user_page(request)


def custom_404_view(request, exception):
    '''
    Renders a custom 404 error page.

    **Parameters**
    - `request`: The HTTP request object.
    - `exception`: The exception that triggered the 404 error.

    **Functionality**
    - Returns the '404.html' template with a 404 status code.
    '''
    return render(
        request,
        '404.html',
        {},
        status=404
    )


def _edit_trip_form(request, trip_id):
    '''
    Handles the editing of an existing trip.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip to be edited.

    **Functionality**
    - Fetches the trip to edit, ensuring it belongs to the logged-in user.
    - Pre-populates and validates the edit form with the trip data.
    - Saves the updated trip if the form is valid, showing success messages.
    - Displays error messages if validation fails.
    '''

    trip = get_object_or_404(Trip, user=request.user, id=trip_id)
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
    '''
    Handles the upload of images for a specific trip.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip to associate images with.

    **Functionality**
    - Retrieves the trip, ensuring it belongs to the logged-in user.
    - Processes the image upload form for POST requests.
    - Saves the image with a reference to the trip if the form is valid.
    - Displays success messages indicating the upload status.
    '''
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


def handle_get_request_edit_trip_page(request, trip_id):
    '''
     Renders the edit trip page with pre-populated trip and image forms.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip to be edited.

    **Functionality**
    - Retrieves the specified trip for the logged-in user.
    - Initializes the edit trip form with current trip data.
    - Provides an empty image upload form.
    - Renders the "edit_trip.html" template with the initialized forms.
    '''
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


def handle_post_request_edit_trip(request, trip_id):
    '''
    Processes the submission of the edit trip form.
    Redirects back to the edit page.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip being edited.

    **Functionality**
    - Calls the `_edit_trip_form` to handle form validation and
        updating of the trip.
    - Redirects to the edit page after processing.
    '''
    _edit_trip_form(request, trip_id)
    return redirect('edit_page', trip_id=trip_id)  # back to edit page


def handle_post_request_upload_image(request, trip_id):
    '''
    Processes the image upload for a specific trip.
    Redirects back to the edit page.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip associated with the uploaded image.

    **Functionality**
    - Calls `_upload_trip_images` to handle image upload and form validation.
    - Redirects to the edit page after processing.
    '''
    _upload_trip_images(request, trip_id)
    return redirect('edit_page', trip_id=trip_id)  # back to edit page


@login_required
def edit_trip_page(request, trip_id):
    '''
    Handles editing operations for a specific user trip,
    requiring authentication.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip to be edited.

    **Functionality**
    - Directs GET requests to render the trip edit page with
        pre-populated forms.
    - Processes POST requests based on the type of form submitted:
      - `editTripForm`: Handles updating trip details.
      - `uploadImageForm`: Handles uploading images associated with the trip.

    **References**
    - Related discussion on handling multiple forms:
    https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django
    '''
    if request.method == 'GET':
        return handle_get_request_edit_trip_page(request, trip_id)
    elif request.method == 'POST':
        if request.POST.get("form_type") == 'editTripForm':
            return handle_post_request_edit_trip(request, trip_id)
        elif request.POST.get("form_type") == 'uploadImageForm':
            return handle_post_request_upload_image(request, trip_id)


def _trip_details(request, trip_id):
    '''
    Retrieves and displays details for a specific user trip.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip to retrieve details for.

    **Functionality**
    - Fetches the trip and associated images for the logged-in user.
    - Renders the "trip_details.html" template with the trip and its images.
    '''
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
    '''
    Displays details of a trip associated with the logged-in user.
    Since it's accessing personal data, the user must be authenticated.
    '''
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
    '''
    Allows users to delete photos.
    This action modifies the user's own data and should be protected.

    **Parameters**
    - `request`: The HTTP request object.
    - `trip_id`: The ID of the trip to be displayed.

    **Functionality**
    - Ensures the user is authenticated.
    - Retrieves the trip and its associated images for the logged-in user.
    - Renders the "trip_details.html" template with trip details and images.
    '''
    image = Image.objects.filter(id=photo_id)
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
