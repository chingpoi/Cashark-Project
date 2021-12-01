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
    path('admindashboard/',views.AdminView.as_view(), name="admindash"),
    path('bankdashboard/',views.BankView.as_view(), name="dashbank"),
    path('bankinfodashboard/',views.BankInfoView.as_view(), name="dashbankinfo"),
    path('feedbackdashboard/',views.FeedbackView.as_view(), name="dashfeedback"),
    path('transactiondashboard/',views.TransactionView.as_view(), name="dashtransaction"),
    path('messagedashboard/',views.MessageView.as_view(), name="dashmessage"),
    path('addressdashboard/',views.AddressView.as_view(), name="dashaddress"),

    #FUNCTIONS
    path('register', views.Functions.Register, name = "register"),
    path('logout', views.Functions.Logout, name="logout"),
    path('userLogin', views.Functions.UserLogin, name = "userLogin"),
    path('bankInfo', views.Functions.BankInfo, name = "bankInfo"),

    #DASHBOARD ADD FUNCTIONS
    path('createUser', views.AdminView.AddUser, name = "userAdd"),
    path('createBank', views.AdminView.AddBank, name = "bankAdd"),
    path('createBankInfo', views.AdminView.AddBankInfo, name = "bankInfoAdd"),
    path('createFeedback', views.AdminView.AddFeedback, name = "feedbackAdd"),
    path('createTransaction', views.AdminView.AddTransaction, name = "transactionAdd"),
    path('createMessage', views.AdminView.AddMessage, name = "messageAdd"),
]