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
    
    #FUNCTIONS
    path('register', views.Functions.Register, name = "register"),
    path('logout', views.Functions.Logout, name="logout"),
    path('userLogin', views.Functions.UserLogin, name = "userLogin"),
    path('bankInfo', views.Functions.BankInfo, name = "bankInfo"),
    path('withdraw', views.Functions.Withdraw, name = "withdraw"),
    path('deposit', views.Functions.Deposit, name = "deposit"),

    #DASHBOARD ADD FUNCTIONS
    path('createUser', views.AdminView.AddUser, name = "userAdd"),
    path('createBank', views.AdminView.AddBank, name = "bankAdd"),
    path('createBankInfo', views.AdminView.AddBankInfo, name = "bankInfoAdd"),
    path('createFeedback', views.AdminView.AddFeedback, name = "feedbackAdd"),
    path('createTransaction', views.AdminView.AddTransaction, name = "transactionAdd"),
    path('createMessage', views.AdminView.AddMessage, name = "messageAdd"),

    #UPDATE FUNCTIONS
    path('updateUser', views.AdminView.UpdateUser, name = "updateUser"),
    path('updateBank', views.AdminView.UpdateBank, name = "updateBank"),
    path('updateBankInfo', views.AdminView.UpdateBankInfo, name = "updateBankInfo"),
    path('updateFeedback', views.AdminView.UpdateFeedback, name = "updateFeedback"),
    path('updateTransactions', views.AdminView.UpdateTransaction, name = "updateTransactions"),
    path('updateMessage', views.AdminView.UpdateMessage, name = "updateMessage"),

    #DELETE FUNCTIONS
    path('deleteUser', views.AdminView.DeleteUser, name = "deleteUser"),
    path('deleteBank', views.AdminView.DeleteBank, name = "deleteBank"),
    path('deleteBankInfo', views.AdminView.DeleteBankInfo, name = "deleteBankInfo"),
    path('deleteFeedback', views.AdminView.DeleteFeedback, name = "deleteFeedback"),
    path('deleteTransactions', views.AdminView.DeleteTransactions, name = "deleteTransactions"),
    path('deleteMessage', views.AdminView.DeleteMessage, name = "deleteMessage"),
]