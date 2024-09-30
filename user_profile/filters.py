import django_filters
from trip.models import Trip


class TripFilter(django_filters.FilterSet):
    class Meta:
        model = Trip
        fields = ['place', 'country',
                  'trip_category', 'trip_status',
                  # 'start_date', 'end_date',
                  'shared']
    
