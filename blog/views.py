from django.shortcuts import render
import datetime as dt

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

def blog_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)