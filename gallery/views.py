from django.shortcuts import render
from trip.models import Image
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def gallery(request):
    '''
    Displays a paginated gallery of shared trip images.

    **Context**
    ``image_list``
        A paginated list of shared :model:`images.Image`

    **Template**
    :template:`gallery/shared_gallery.html`

    **Functionality**
    - Retrieves all images marked as shared.
    - Paginates the images, 6 per page.
    - Handles page navigation errors to ensure valid page rendering.
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
