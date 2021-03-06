"""CasharkProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CasharkApp.urls',namespace="index")),
    path('about/', include('CasharkApp.urls',namespace="about")),
    path('blog-single/', include('CasharkApp.urls',namespace="blog-single")),
    path('blog/', include('CasharkApp.urls',namespace="blog")),
    path('contact/', include('CasharkApp.urls',namespace="contact")),
    path('login/', include('CasharkApp.urls',namespace="login")),
    path('portfolio/', include('CasharkApp.urls',namespace="portfolio")),
    path('services/', include('CasharkApp.urls',namespace="services")),
    path('blog-double/',include('CasharkApp.urls',namespace="blog-double")),
    path('user-profile/',include('CasharkApp.urls',namespace="profile")),
    path('admindashboard/',include('CasharkApp.urls',namespace="admindash")),
    path('bankdashboard/',include('CasharkApp.urls',namespace="dashbank")),
    path('bankinfodashboard/',include('CasharkApp.urls',namespace="dashbankinfo")),
    path('feedbackdashboard/',include('CasharkApp.urls',namespace="dashfeedback")),
    path('transactiondashboard/',include('CasharkApp.urls',namespace="dashtransaction")),
    path('messagedashboard/',include('CasharkApp.urls',namespace="dashmessage")),
    path('addressdashboard/',include('CasharkApp.urls',namespace="dashaddress")),
]

urlpatterns += staticfiles_urlpatterns()