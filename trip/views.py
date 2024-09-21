from django.shortcuts import render
from django.views import generic
from .models import (Trip, Activity, Comment, Note, Image)

# Create your views here.


# Create your views here.
def landing_page(request):
    '''
    View for Landing page
    '''
    
    return render(request, "trip/landing_page.html")
