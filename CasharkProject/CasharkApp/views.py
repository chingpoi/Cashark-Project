from django.shortcuts import redirect, render
from django.views.generic import View

# Create your views here.
class AboutView(View):
	def get(self,request):
		return render(request,'about.html')

class BlogSingleView(View):
	def get(self,request):
		return render(request,'blog.html')

class BlogView(View):
	def get(self,request):
		return render(request,'contact.html')

class ContactView(View):
	def get(self,request):
		return render(request,'index.html')

class IndexView(View):
	def get(self,request):
		return render(request,'login.html')

class LoginView(View):
	def get(self,request):
		return render(request,'portfolio.html')

class PortfolioView(View):
	def get(self,request):
		return render(request,'services.html')

class ServicesView(View):
	def get(self,request):
		return render(request,'index.html')
