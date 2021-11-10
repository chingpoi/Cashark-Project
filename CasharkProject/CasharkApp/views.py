from django.shortcuts import redirect, render
from django.views.generic import View

# Create your views here.
class AboutView(View):
	def get(self,request):
		return render(request,'about.html')

class BlogSingleView(View):
	def get(self,request):
		return render(request,'blog-single.html')

class BlogView(View):
	def get(self,request):
		return render(request,'blog.html')

class ContactView(View):
	def get(self,request):
		return render(request,'contact.html')

class IndexView(View):
	def get(self,request):
		return render(request,'index.html')

class LoginView(View):
	def get(self,request):
		return render(request,'login.html')

class PortfolioView(View):
	def get(self,request):
		return render(request,'portfolio.html')

class ServicesView(View):
	def get(self,request):
		return render(request,'services.html')
