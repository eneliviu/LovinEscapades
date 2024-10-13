from geopy import geocoders
from geopy.exc import GeocoderTimedOut


def get_coordinates(location, attempt=1, max_attempts=5):
    '''
    Geocodes an address with retry on timeout.
    GeoPy documentation:
    https://geopy.readthedocs.io/en/latest/#geopy.exc.GeocoderTimedOut

    Parameters:
    location (str): The location to geocode.
    attempts (int, optional): Current retry attempt. Default is 1.
    max_attempts (int, optional): Maximum retry attempts. Default is 5.

    Returns:
    tuple: Geocoded location data (Latitude and Longitude).

    Raises:
    GeocoderTimedOut: If the max number of attempts is exceeded.
    '''
    geocoder = geocoders.Nominatim(user_agent='trip')
    try:
        get_location = geocoder.geocode(location, exactly_one=True,
                                        language='en')

        if get_location:
            return get_location.latitude, get_location.longitude
        else:
            # raise ValueError("Could not geocode the location")
            return "location-error"
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            print(f"Attempt {attempt} failed; retrying...")
            return get_coordinates(location,
                                   attempt=attempt+1,
                                   max_attempts=max_attempts)
        # raise GeocoderTimedOut("Max attempts exceeded")
        return 'max-attempts-exceeded-error'


# class About(models.Model):
#     """
#     Stores a single about me text
#     """
#     title = models.CharField(max_length=200)
#     profile_image = CloudinaryField('image', default='placeholder')
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()

#     def __str__(self):
#         return self.title


# class ContactUs(models.Model):
#     """
#     Stores a single collaboration request message
#     """
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     message = models.TextField()
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Collaboration request from {self.name}"
