from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image

# posts = [
#     {
#         'author': 'VivNK',
#         'title': 'Blog post 1',
#         'content':'First blog',
#         'date_posted':'July 19,2019'
#     }
# ]
    

# Create your views here.
def welcome(request):
    # context = {
    #     'posts':posts
    # }
    return render(request, 'blog/welcome.html', )

def about(request):
     return render(request, 'blog/about.html',{'title':'About'})
 
def blog_current(request):
    date = dt.date.today()
    blog = Image.imagepost_current()
    return render(request, 'blog/imagepost_current.html', {"date": date,"blog":blog})

def past_image_blog(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(blog_current)

    blog = Image.days_blog(date)
    return render(request, 'blog/imagepost_past.html',{"date": date,"blog":blog})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
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