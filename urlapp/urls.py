
from django.urls import path,include
from urlapp import views as v

urlpatterns = [

    path('',v.index,name="index")

]