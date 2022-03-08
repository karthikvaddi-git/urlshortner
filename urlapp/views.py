from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners
import qrcode
from .models import  *

from pyqrcode import create
import png
import os
import base64
from pyqrcode import create
import png


def embed_QR(url_input, name):
    embedded_qr = create(url_input)
    embedded_qr.png(name, scale=7)



# Create your views here.
def index(request):

    if request.method=='POST':
        print(request.POST['urlshortner'])
        urlvar=request.POST['urlshortner']
        s = pyshorteners.Shortener()
        names=s.tinyurl.short(urlvar)
        name="temp"
        name += ".png"
        embed_QR(names, name)
        with open(name, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return render(request, 'urlpage.html', {'image': image_data})












    if request.method=='GET':
        return render(request, "index.html")


