from geopy import geocoders
from geopy.exc import GeocoderTimedOut


def get_coordinates(location, attempt=1, max_attempts=5):
    '''
    Geocodes an address with retry on timeout.
    GeoPy documentation: https://geopy.readthedocs.io/en/latest/#geopy.exc.GeocoderTimedOut
    
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
        # print("Address 1:",location.latitude, location.longitude)
        if location:
            return get_location.latitude, get_location.longitude
        else:
            raise ValueError("Could not geocode the location")
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            print(f"Attempt {attempt} failed; retrying...")
            return get_coordinates(location,
                                   attempt=attempt+1,
                                   max_attempts=max_attempts)
        raise GeocoderTimedOut("Max attempts exceeded")


