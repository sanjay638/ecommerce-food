"""Ecommerce_Food_Products_Sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.conf.urls import url
from django.urls import re_path
from django.conf.urls.static import static

from Ecommerce_Food_Products_Sales import settings
from Customer import views as Customer_views
from Owner import views as admin_views

urlpatterns = [
        re_path(r'^admin/', admin.site.urls),

        re_path(r'^$',Customer_views.index,name='home'),

        re_path(r'^userlogin/$', Customer_views.userlogin, name="userlogin"),
        re_path(r'^register/$', Customer_views.register, name="register"),
        re_path(r'^viewdetails/$', Customer_views.viewdetails, name="viewdetails"),
        re_path(r'^contactus/$', Customer_views.contactus, name="contactus"),
        re_path(r'^viewmodeldetails/(?P<pk>\d+)/$', Customer_views.viewmodeldetails, name="viewmodeldetails"),
        re_path(r'^addtocard/(?P<pk>\d+)/$', Customer_views.addtocard, name="addtocard"),
        re_path(r'^feedback/$', Customer_views.feedback, name="feedback"),
        re_path(r'^mydetails',Customer_views.mydetails, name="mydetails"),
        re_path(r'^updatedetails',Customer_views.updatedetails, name="updatedetails"),
        re_path(r'^userchart/(?P<chart_type>\w+)', Customer_views.userchart, name="userchart"),
        re_path(r'^reviewspage/$',Customer_views.reviewspage, name="reviewspage"),
        re_path('^ordertacking/$', Customer_views.ordertacking, name="ordertacking"),
        re_path(r'^orderchart/(?P<schart_type>\w+)', Customer_views.orderchart, name="orderchart"),
        re_path('^userlogout/$', Customer_views.userlogout, name="userlogout"),
        re_path('^linear/$', Customer_views.linear, name="linear"),






        re_path(r'^adminlogin/$',admin_views.adminlogin, name="adminlogin"),
        re_path(r'^uploadpage/$',admin_views.uploadpage, name="uploadpage"),
        re_path(r'^adminregister/$',admin_views.adminregister,name="adminregister"),
        re_path(r'^updatefood/$', admin_views.updatefood, name="updatefood"),
        re_path(r'^viewfeedback/$',admin_views.viewfeedback,name="viewfeedback"),
        re_path(r'^customerdetails/$',admin_views.customerdetails,name="customerdetails"),
        re_path(r'^foodchart/(?P<chart_type>\w+)', admin_views.foodchart, name="foodchart"),
        re_path('^adminlogout/$', admin_views.adminlogout, name="adminlogout"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

