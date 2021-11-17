from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'CasharkApp'
urlpatterns = [ 
#URLs for Cashshark app
    path('', views.IndexView.as_view(), name="Index"),
    path('About/', views.AboutView.as_view(), name="About"),
    path('BlogSingle/', views.BlogSingleView.as_view(), name="BlogSingle"),
    path('Blog/', views.BlogView.as_view(), name="Blog"),
    path('Contact/', views.ContactView.as_view(), name="Contact"),
    path('Login/', views.LoginView.as_view(), name="Login"),
    path('Portfolio/', views.PortfolioView.as_view(), name="Portfolio"),
    path('Services/', views.ServicesView.as_view(), name="Services"),
    path('BlogDouble/',views.BlogDoubleView.as_view(), name="BlogDouble"),
    path('UserProfile/',views.ProfileView.as_view(), name="Profile"),

    #FUNCTIONS
    path('register', views.Functions.Register, name = "register"),
    path('logout', views.Functions.Logout, name="logout"),
    path('userLogin', views.Functions.UserLogin, name = "userLogin"),
]