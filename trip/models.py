from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.dispatch import receiver  # to create Profile instance
from cloudinary.models import CloudinaryField
from user_profile.models import Profile
from . utils import get_coordinates

'''
**blank=True**: Specifies that the field is optional.
- The field is allowed to be empty in forms. It's used for form validation

**null=True**: controls whether the database column allows `NULL` values.
- Use this for fields that are not required in the database.

Usually, both `blank=True` and `null=True` are used together for fields where
you want to allow empty values both in the database and in forms. However,
for `CharField` and `TextField`, it's generally recommended to use
only `blank=True` and not `null=True`.

### When to Use `null=True`:
- For non-string-based fields, such as `DateTimeField`, `IntegerField`,
    `ForeignKey`, etc., where a field might be optional and you would like it
    to be stored as NULL in the database.
- Avoid using `null=True` for `CharField` and `TextField` fields to avoid
    confusing behavior. Instead, use `blank=True` for form validation and
    allow the empty string to indicate the absence of data.

### Summary
1. **String Fields (`CharField` and `TextField`):**
   - Use `blank=True` to allow forms to submit empty values.
   - Do not use `null=True` to keep data handling consistent and
   avoid storing NULL values in string fields.

2. **Non-String Fields:**
   - Use both `blank=True` and `null=True` for optional fields
   to allow NULL values in the database.

### Relationships:
ForeignKey field type defines a many-to-one relationship

'''


class Trip(models.Model):
    TRIP_CATEGORY = (('Leisure', 'LEISURE'),
                     ('Business', 'BUSINESS'),
                     ('Adventure', 'ADVENTURE'),
                     ('Family', 'FAMILY'),
                     ('Romantic', 'ROMANTIC'))
    TRIP_STATUS = (("Completed", 'COMPLETED'),
                   ("Ongoing", "ONGOING"),
                   ("Planned", 'PLANNED'))
    SHARE_CHOICES = (("Yes", "YES"),
                     ("NO", 'No'))

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='trips')
    title = models.CharField(
        max_length=100,
        blank=False,
        validators=[MinLengthValidator(2)]
    )

    # Optional field,stored as an empty string if left blank
    # description = models.TextField(blank=True)

    place = models.CharField(
        max_length=100,
        blank=False,
        validators=[MinLengthValidator(2)]
        )
    country = models.CharField(
        max_length=100,
        blank=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(56)
            ]
        )
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    trip_category = models.CharField(max_length=50,
                                     choices=TRIP_CATEGORY,
                                     default='LEISURE')
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    trip_status = models.CharField(choices=TRIP_STATUS, default='PLANNED')
    shared = models.CharField(max_length=3,
                              choices=SHARE_CHOICES,
                              default='YES')

    # Raise Validation Error In Model Save Method:
    # https://ilovedjango.com/django/models-and-databases/tips/sub/raise-validation-error-in-model-save-method/

    is_cleaned = False

    def clean(self):
        self.is_cleaned = True
        coords = get_coordinates(self.place)

        if coords == 'location-error':
            raise ValidationError("Error: could not geocode the location")
        else:
            self.lat = coords[0]
            self.lon = coords[1]
        super(Trip, self).clean()

    def save(self, *args, **kwargs):
        '''
        Override the save() method to set the Lat and Lon values
        before saving.
        '''
        if not self.is_cleaned:
            self.full_clean()
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.trip_category} trip to {self.place}, {self.country}'

    class Meta:
        ordering = ["-created_on", 'country', 'start_date']


class Image(models.Model):
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='images')
    # image = models.ImageField(upload_to='trip_images/')
    title = models.CharField(
        max_length=50,
        blank=False,
        validators=[MinLengthValidator(2)])
    image = CloudinaryField('image', default=None, blank=False)
    description = models.TextField(
        blank=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(500)
            ]
        )
    shared = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo for {self.trip.title}, {self.trip.place},\
                 {self.trip.country}'

    class Meta:
        ordering = ["-uploaded_at"]


# Create user profile when a new user registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    Create profile for new user automatically
    '''
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # User follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
# post_save.connect(create_profile, sender=User)
