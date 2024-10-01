from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from .models import Trip


class AddTripForm(forms.ModelForm):
    '''
    Model form for new Trip submission.
    Pass the user to the form and use it in the `clean` method.
    '''

    # def __init__(self, user, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     self.request = kwargs.pop('request', None)
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Trip
        exclude = ('user', 'lat', 'lon', 'created_on', 'status',)
        widgets = {
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 40})
        }
        
    # Server-side validation:
    def clean(self, *args, **kwargs):
        '''
        - Add custom validation to ensure that `end_date` and
        `start_date` are appropriate for the selected trip category:
        - Check for partial time interval overlaps:
            - `start_date__lte=end_date` ensures the start date of the
                existing trip is before or on the end date of the new trip.
            - `end_date__gte=start_date` ensures the end date of the existing
                trip is after or on the start date of the new trip.
            - don't check overlaps with completed trips as they
                don't affect planning
        '''
        cleaned_data = super(AddTripForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        current_date = timezone.now().date()
        selected_option = cleaned_data.get('trip_status')
        
        # Check if end date is earlier than start date
        if end_date < start_date:
            errMsg = 'End date cannot be earlier than start date'
            raise ValidationError(errMsg)
        
        # Validate dates for Planned trips
        if ((selected_option == 'Planned') and
           (start_date < current_date)):
            errMsg = "Error: Cannot plan a trip on past dates."
            raise ValidationError(errMsg)
        
        # Validate dates for Ongoing trips
        if ((selected_option == 'Ongoing') and 
           ((current_date < start_date) or (current_date > end_date))):
            errMsg = "Error: Ongoing trip must include the current date."
            raise ValidationError(errMsg)
        
        # Validate dates for Completed trips
        if ((selected_option == 'Completed') and
           ((start_date > current_date) or (current_date < end_date))):
            errMsg = "Error: Completed trip end date cannot past current date."
            raise ValidationError(errMsg)

        # Initialize overlapping_trips to an empty queryset
        collide_trips = Trip.objects.none()

        # This query checks:
        # `start_date__lte=end_date`: trips starts on/before new trip ends.
        # `end_date__gte=start_date`: trips ends on/after new trip starts.
        
        collide_trips = Trip.objects.filter(
                                    Q(start_date__lte=start_date,
                                        end_date__gte=end_date) |
                                    Q(start_date__lte=end_date,
                                        end_date__gte=start_date)
                                            )
        collide_trips = collide_trips.exclude(trip_status__in=['Completed',
                                                               'Ongoing'])
        collide_trips = collide_trips.exclude(id=self.instance.id
                                              if self.instance
                                              else None)
        if collide_trips.exists():
            errMsg = 'These dates overlap with another trip.'
            raise ValidationError(errMsg)

        super().clean(*args, **kwargs)


class TripSelectionForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ('trip_status', 'trip_category',)

    # TRIP_STATUS = (("Completed", 'COMPLETED'),
    #                ("Ongoing", "ONGOING"),
    #                ("Planned", 'PLANNED'))

    # TRIP_CATEGORY = (('Leisure', 'LEISURE'),
    #                  ('Business', 'BUSINESS'),
    #                  ('Adventure', 'ADVENTURE'),
    #                  ('Family', 'FAMILY'),
    #                  ('Romantic', 'ROMANTIC'))
    
    # trip_status = forms.ChoiceField(choices=TRIP_STATUS, required=True)
    # trip_category = forms.ChoiceField(choices=TRIP_CATEGORY, required=True)

