from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners



# Create your views here.
def index(request):
    if request.method=='POST':
        print(request.POST['urlshortner'])
        urlvar=request.POST['urlshortner']
        s = pyshorteners.Shortener()
        shorturl=s.tinyurl.short(urlvar)

        return HttpResponse(shorturl)



    if request.method=='GET':
        return render(request, "index.html")


