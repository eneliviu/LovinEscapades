from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.
class ContactUs(models.Model):

    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        blank=False
    )
    email = models.EmailField()
    message = models.TextField(
         validators=[
            MinLengthValidator(50),
            MaxLengthValidator(500)]
    )
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Inquiry from {self.name}"
