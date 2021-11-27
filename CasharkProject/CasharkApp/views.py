from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import *
from django.http import HttpResponse

# Create your views here.
class AboutView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'about.html',context)
		except KeyError:
			pass
		return render(request,'about.html')
		

class BlogSingleView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'blog-single.html',context)
		except KeyError:
			pass
		return render(request,'blog-single.html')

class BlogDoubleView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'blog-double.html',context)
		except KeyError:
			pass
		return render(request,'blog-double.html')

class BlogView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'blog.html',context)
		except KeyError:
			pass
		return render(request,'blog.html')

class ContactView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'contact.html',context)
		except KeyError:
			pass
		return render(request,'contact.html')

class IndexView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'index.html',context)
		except KeyError:
			pass
		return render(request,'index.html')


class LoginView(View):
	def get(self,request):

		return render(request,'login.html')

class PortfolioView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'portfolio.html',context)
		except KeyError:
			pass
		return render(request,'portfolio.html')

class ServicesView(View):
	def get(self,request):
		try:
			request.session['User_ID']
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
			}
			return render(request,'services.html',context)
		except KeyError:
			pass
		return render(request,'services.html')

class ProfileView(View):
	def get(self,request):
		currentUser = User.objects.get(User_ID = request.session['User_ID'])

		user = User.objects.get(User_ID = currentUser.User_ID)
		bankInfo = BankInfo.objects.all()
		transaction = Transaction.objects.all()
		message = Message.objects.all()
		bank = Bank.objects.all()


		context = {
			'user': user,
			'bankInfo': bankInfo,
			'transaction': transaction,
			'message': message,
			'bank': bank,
		}
		return render(request,'profile.html',context)

class AdminView(View):
	def get(self,request):
		currentUser = User.objects.get(User_ID = request.session['User_ID'])

		user = User.objects.all()
		bankInfo = BankInfo.objects.all()
		transaction = Transaction.objects.all()
		message = Message.objects.all()
		bank = Bank.objects.all()
	
		context = {
			'user': user,
			'bankInfo': bankInfo,
			'transaction': transaction,
			'message': message,
			'bank': bank,
		}
		return render(request,'userdash.html',context)

class BankView(View):
	def get(self,request):
		
		return render(request,'bankdash.html')

class BankInfoView(View):
	def get(self,request):
		
		return render(request,'dashbankinfo.html')

class FeedbackView(View):
	def get(self,request):
		
		return render(request,'dashfeedback.html')

class TransactionView(View):
	def get(self,request):
		
		return render(request,'dashtransaction.html')

class MessageView(View):
	def get(self,request):
		
		return render(request,'dashmessage.html')

class AddressView(View):
	def get(self,request):
		
		return render(request,'dashaddress.html')

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
					
					form = User(First_Name = firstName, Last_Name = lastName, Email = email,  Password = password, Birthdate = birthdate, Mobile_Number = mobileNumber, Balance = 0, Credit_Score = 0, Address_Province = aProvince, Address_City = aCity, Address_Street = aStreet)
					form.save()

					user = User.objects.get(Email = email)

					request.session['User_ID'] = user.User_ID
					return redirect('http://127.0.0.1:8000/user-profile')
				else:
					print(form.errors)
					return HttpResponse('not valid')

	def Logout(request):
		del request.session['User_ID']
		return redirect('http://127.0.0.1:8000/')

	def UserLogin(request):
		if request.method == "POST":
			user = User.objects.get(Email = request.POST['Email'])
			if user.Password == request.POST['Password']:
				request.session['User_ID'] = user.User_ID

				return redirect('http://127.0.0.1:8000/user-profile')
			else:
				return HttpResponse("Your Email and Password do not Match.")

	def BankInfo(request):
			if request.method == "POST":
				form = AddBankForm(request.POST)
				if form.is_valid():
					user = request.POST.get("User_ID")
					userID = User.objects.get(User_ID = user)

					bank = request.POST.get("Bank")
					accountNumber = request.POST.get("Account_Number")

					form = BankInfo(User_ID = userID, Bank = bank)
					form.save()

					bankInfoID = BankInfo.objects.filter(User_ID = userID, Bank = bank).first()
					
					form = Bank(Bank_Info_ID = bankInfoID, Account_Number = accountNumber, Balance = 5000)
					form.save()
					return redirect('http://127.0.0.1:8000/user-profile')
				else:
					print(form.errors)
					return HttpResponse('not valid')


				