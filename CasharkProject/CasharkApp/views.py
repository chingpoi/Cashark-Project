from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from .forms import *
from django.http import HttpResponse

# Create your views here.
class AboutView(View):
	def get(self,request):
		return render(request,'about.html')

class BlogSingleView(View):
	def get(self,request):
		return render(request,'blog-single.html')

class BlogDoubleView(View):
	def get(self,request):
		return render(request,'blog-double.html')

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

class ProfileView(View):
	def get(self,request):
		return render(request,'profile.html')


#Functions
class Functions(View):
	def Register(request):
			if request.method == "POST":
				form = UserForm(request.POST)
				if form.is_valid():
					firstName = request.POST.get("FirstName")
					lastName = request.POST.get("LastName")
					email = request.POST.get("Email")
					password = request.POST.get("Password")


					form = User(FirstName = firstName, LastName = lastName, Email = email,  Password = password)
					form.save()

					request.session['FirstName'] = firstName

					return redirect('http://127.0.0.1:8000/')
				else:
					print(form.errors)
					return HttpResponse('not valid')

	def Logout(request):
		try:
			del request.session['FirstName']
		except KeyError:
			pass
		return redirect('http://127.0.0.1:8000/')

	def UserLogin(request):
		if request.method == "POST":
			user = User.objects.get(Email = request.POST['Email'])
			if user.Password == request.POST['Password']:
				request.session['FirstName'] = user.FirstName
				return redirect('http://127.0.0.1:8000/')
			else:
				return HttpResponse("You're Email and Password do not Match bruh.")


				