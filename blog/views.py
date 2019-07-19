from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('<h1>Welcome to the Photoblog</h1>')

def about(request):
    return HttpResponse('<h1>About Photoblog</h1>')


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