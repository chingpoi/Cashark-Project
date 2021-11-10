from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'CashsharkApp'
urlpatterns = [ 
#URLs for Cashshark app
    path('', views.IndexView.as_view(), name="index"),

]