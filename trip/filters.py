import django_filters
# from django import forms
from trip.models import Trip


class TripFilter(django_filters.FilterSet):
    
    # https://stackoverflow.com/questions/66964037/boolean-field-for-django-filter-search-bar
    # shared__exact = django_filters.BooleanFilter(
    #     field_name='shared',
    #     label='Shared',
    #     lookup_expr='exact',
    #     widget=forms.CheckboxInput,
    # )
    # place = CharFilter(label='City/Location')
    # country = CharFilter(label='Country')
    # trip_category = CharFilter(label='Category')
    # trip_status = CharFilter(label='Status')

    class Meta:
        model = Trip
        fields = {'place': ['icontains'],
                  'country': ['icontains'],
                  'trip_category': ['exact'],
                  'trip_status': ['exact'],
                  # 'shared': ['exact'],
                  # 'start_date', 'end_date',
                  }

