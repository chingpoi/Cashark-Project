from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'CasharkApp'
urlpatterns = [ 
#URLs for Cashshark app
    path('', views.IndexView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('blog-single/', views.BlogSingleView.as_view(), name="blog-single"),
    path('blog/', views.BlogView.as_view(), name="blog"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolio"),
    path('services/', views.ServicesView.as_view(), name="services"),
    path('blog-double/',views.BlogDoubleView.as_view(), name="blog-double"),
    path('user-profile/',views.ProfileView.as_view(), name="profile"),

    #FUNCTIONS
    path('register', views.Functions.Register, name = "register"),
    path('logout', views.Functions.Logout, name="logout"),
    path('userLogin', views.Functions.UserLogin, name = "userLogin"),
]