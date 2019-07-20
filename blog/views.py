from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image
    

# Create your views here.
def welcome(request):
    blog = Image.objects.all()
    date = dt.date.today()
    return render(request, 'blog/welcome.html', )

def about(request):
     return render(request, 'blog/about.html',{'title':'About'})
 
# def blog_current(request):
#     date = dt.date.today()
#     blog = Image.get_image_by_id()
#     return render(request, 'blog/blog-current.html', {"date": date,"blog":blog})


def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_name(search_term)
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