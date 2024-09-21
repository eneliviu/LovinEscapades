from django.db import models
from django.contrib.auth.models import User

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
    TRIP_CATEGORY = (('LEISURE', 'Leisure'),
                     ('BUSINESS', 'Business'),
                     ('ADVENTURE', 'Adventure'),
                     ('FAMILY', 'Family'),
                     ('ROMANTIC', 'Romantic'))
    TRIP_STATUS = ((0, "Finished"),
                   (1, "Ongoing"),
                   (2, "Planned"))

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='trips')
    title = models.CharField(max_length=100)

    # Optional field,stored as an empty string if left blank
    description = models.TextField(blank=True)

    place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    trip_category = models.CharField(max_length=50, choices=TRIP_CATEGORY)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    trip_status = models.IntegerField(choices=TRIP_STATUS, default=0)
    shared = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        '''
        Override the save() method to set the Lat and Lon values 
        before saving.
        '''
        try:
            coords = get_coordinates(self.location)
            self.lat = coords[0]
            self.lon = coords[1]
        except Exception as e:
            print(f"Operation failed: {e}")
    
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.trip_category} trip to {self.place}, {self.country}'

    class Meta:
        ordering = ["-created_on", 'start_date', 'country']


class Activity(models.Model):
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='activities')
    name = models.CharField(max_length=255)

    # Optional field,stored as an empty string if left blank
    description = models.TextField(blank=True)

    date = models.DateField()

    def __str__(self):
        return self.name


class AbstractPostModel(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='%(class)ss')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_on"]  # descending order of creation date


class Comment(AbstractPostModel):
    COMMENT_STATUS = ((0, "Draft"),
                      (1, "Published"))
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='comments')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.user.username} for \
                            {self.trip.user} on \
                            "{self.trip.title}" post'


class Note(AbstractPostModel):
    NOTE_STATUS = ((0, "Draft"),
                   (1, "Published"))
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='notes')
    status = models.IntegerField(choices=NOTE_STATUS,
                                 default=0)

    def __str__(self):
        return f'Post by {self.user.username} on {self.trip.title}'


class Image(models.Model):
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField() # upload_to='trip_images/'

    # Optional field,stored as an empty string if left blank
    description = models.TextField(blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image for {self.trip.name} uploaded at {self.uploaded_at}'

    class Meta:
        ordering = ["-uploaded_at"]