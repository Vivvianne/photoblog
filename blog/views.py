from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image
    

# Create your views here.
def welcome(request):
    images = Image.get_all_images()
    date = dt.date.today()
    return render(request, 'blog/index.html', {'images':images} )

def about(request):
     return render(request, 'blog/about.html',{'title':'About'})
 


def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        # searched_images = Image.search_by_image_name(search_term)
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'blog/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'blog/search.html',{"message":message})
    
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"blog/image.html", {"image":image})