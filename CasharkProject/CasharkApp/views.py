from django.shortcuts import redirect, render
from django.views.generic import View
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
				form = RegisterForm(request.POST)
				if form.is_valid():
					firstName = request.POST.get("First_Name")
					lastName = request.POST.get("Last_Name")
					email = request.POST.get("Email")
					password = request.POST.get("Password")
					birthdate = request.POST.get("Birthdate")
					mobileNumber = request.POST.get("Mobile_Number")

					aProvince = request.POST.get("Address_Province")
					aCity = request.POST.get("Address_City")
					aStreet = request.POST.get("Address_Street")

					form = Address(Address_Province = aProvince, Address_City = aCity, Address_Street = aStreet)
					form.save()

					AddressID = Address.objects.get(Address_Province = aProvince, Address_City = aCity, Address_Street = aStreet)
					
					form = User(First_Name = firstName, Last_Name = lastName, Email = email,  Password = password, Birthdate = birthdate, Mobile_Number = mobileNumber, Address_ID = AddressID, Balance = 0, Credit_Score = 0)
					form.save()

					user = User.objects.get(Email = email)

					request.session['User_ID'] = user.User_ID
					request.session['First_Name'] = user.First_Name
					request.session['Last_Name'] = user.Last_Name
					request.session['Email'] = user.Email
					request.session['Birthdate'] = user.Birthdate
					request.session['Mobile_Number'] = user.Mobile_Number
					request.session['Balance'] = user.Balance
					request.session['Credit_Score'] = user.Credit_Score

					request.session['Address_Province'] = user.Address_ID.Address_Province
					request.session['Address_City'] = user.Address_ID.Address_City
					request.session['Address_Street'] = user.Address_ID.Address_Street


					return redirect('http://127.0.0.1:8000/user-profile')
				else:
					print(form.errors)
					return HttpResponse('not valid')

	def Logout(request):
		del request.session['First_Name']
		return redirect('http://127.0.0.1:8000/')

	def UserLogin(request):
		if request.method == "POST":
			user = User.objects.get(Email = request.POST['Email'])
			if user.Password == request.POST['Password']:
				request.session['User_ID'] = user.User_ID
				request.session['First_Name'] = user.First_Name
				request.session['Last_Name'] = user.Last_Name
				request.session['Email'] = user.Email
				request.session['Birthdate'] = user.Birthdate
				request.session['Mobile_Number'] = user.Mobile_Number
				request.session['Balance'] = user.Balance
				request.session['Credit_Score'] = user.Credit_Score

				request.session['Address_Province'] = user.Address_ID.Address_Province
				request.session['Address_City'] = user.Address_ID.Address_City
				request.session['Address_Street'] = user.Address_ID.Address_Street
				
				return redirect('http://127.0.0.1:8000/user-profile')
			else:
				return HttpResponse("Your Email and Password do not Match.")


				