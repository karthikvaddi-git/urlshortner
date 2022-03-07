from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners
import qrcode
from .models import  *


# Create your views here.
def index(request):
    if request.method=='POST':
        print(request.POST['urlshortner'])
        urlvar=request.POST['urlshortner']
        s = pyshorteners.Shortener()
        shorturl=s.tinyurl.short(urlvar)
        input_data = shorturl
        # Creating an instance of qrcode
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)

        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white',, embeded_image_path="/media/images/{shorturl}")
        #img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/image.png")
        img.save()
        modelobj=qrcodemodel(name=shorturl,qrimage=img.save("qrco)
        modelobj.save()
        print(modelobj)

        print(shorturl)
      #  data={'shorturl':shorturl,'img':img}
       # print(data['shorturl'])
       # print(data['img'])



        return render(request,"urlpage.html",{"modelobj":modelobj,"shorturl":shorturl})




    if request.method=='GET':
        return render(request, "index.html")


