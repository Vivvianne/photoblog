from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image

posts = [
    {
        'author': 'VivNK',
        'title': 'Blog post 1',
        'content':'First blog',
        'date_posted':'July 19,2019'
    }
]
    

# Create your views here.
def welcome(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/welcome.html', context)

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