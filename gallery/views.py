from django.shortcuts import render, get_object_or_404
from trip.models import Image
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def gallery(request):
    '''
    Renders the most recent information on the website
    and allows user inqueries.

    **Context**
    ``contact_form``
        An instance of :form:`contact.ContactForm`
    **Template**
        :template:`contact/about.html`
    '''
    images = Image.objects.filter(shared=True)
    paginator = Paginator(images, 6)  # 6 trips in each page
    page = request.GET.get('page')
    try:
        image_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        image_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        image_list = paginator.page(paginator.num_pages)

    return render(
        request,
        'gallery/shared_gallery.html',
        context={
            'page': page,
            'image_list': image_list,
        }
    )
