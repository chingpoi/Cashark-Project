from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import *
from django.http import HttpResponse
import datetime

# Create your views here.
class AboutView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'About': 'active',
				'isAdmin': isAdmin
			}
			return render(request,'about.html',context)
		except KeyError:
			pass
		return render(request,'about.html',{'About': 'active'})
		

class BlogSingleView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'isAdmin': isAdmin
			}
			return render(request,'blog-single.html',context)
		except KeyError:
			pass
		return render(request,'blog-single.html')

class BlogDoubleView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'isAdmin': isAdmin
			}
			return render(request,'blog-double.html',context)
		except KeyError:
			pass
		return render(request,'blog-double.html')

class BlogView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'Blog': 'active',
				'isAdmin': isAdmin
			}
			return render(request,'blog.html',context)
		except KeyError:
			pass
		return render(request,'blog.html',{'Blog': 'active'})

class ContactView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'SignUp': 'active',
				'isAdmin': isAdmin
			}
			return render(request,'contact.html',context)
		except KeyError:
			pass
		return render(request,'contact.html',{'SignUp': 'active'})

class IndexView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'Index': 'active',
				'isAdmin': isAdmin
			}
			return render(request,'index.html',context)
		except KeyError:
			pass
		return render(request,'index.html',{'Index': 'active'})


class LoginView(View):
	def get(self,request):

		return render(request,'login.html',{'Login': 'active'})

class PortfolioView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'Portfolio': 'active',
				'isAdmin': isAdmin
			}
			return render(request,'portfolio.html',context)
		except KeyError:
			pass
		return render(request,'portfolio.html',{'Portfolio': 'active'})

class ServicesView(View):
	def get(self,request):
		try:
			isAdmin = False
			request.session['User_ID']
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			context = {
				'user': user,
				'Service': 'active',
				'isAdmin': isAdmin
			}
			return render(request,'services.html',context)
		except KeyError:
			pass
		return render(request,'services.html',{'Service': 'active'})

class ProfileView(View):
	def get(self,request):
		isAdmin = False
		if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
			isAdmin = True
		currentUser = User.objects.get(User_ID = request.session['User_ID'])

		user = User.objects.get(User_ID = currentUser.User_ID)
		bankInfo = BankInfo.objects.filter(User_ID = user)
		transaction = Transaction.objects.all()
		message = Message.objects.all()
		bank = Bank.objects.all()


		context = {
			'user': user,
			'bankInfo': bankInfo,
			'transaction': transaction,
			'message': message,
			'bank': bank,
			'Profile': 'active',
			'isAdmin': isAdmin
		}
		return render(request,'profile.html',context)

class AdminView(View):
	def get(self,request):
		try:
			isAdmin = False
			if(AdminList.objects.filter(User_ID = request.session['User_ID']).exists()):
				isAdmin = True
			currentUser = User.objects.get(User_ID = request.session['User_ID'])
			user = User.objects.get(User_ID = currentUser.User_ID)
			users = User.objects.exclude(User_ID = user.User_ID)
			bankInfo = BankInfo.objects.all()
			transaction = Transaction.objects.all()
			message = Message.objects.all()
			bank = Bank.objects.all()
			feedback = Feedback.objects.all()
			admin = AdminList.objects.all()
			context = {
				'user': user,
				'users': users,
				'bankInfo': bankInfo,
				'transaction': transaction,
				'message': message,
				'bank': bank,
				'feedback': feedback,
				'admin':admin,
				'Admin': 'active',
				'isAdmin': isAdmin
			}
			return render(request,'userdash.html',context)
		except KeyError:
			pass
		return render(request,'userdash.html')

	#FOR ADD USER
	def AddUser(request):
		if request.method == "POST":
			form = UserForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#PRIMARY USER ATTRIBUTES
				uFname = request.POST.get("First_Name")
				uLname = request.POST.get("Last_Name")
				uMobile = request.POST.get("Mobile_Number")
				uEmail = request.POST.get("Email")
				uPassword = request.POST.get("Password")
				uBirthdate = request.POST.get("Birthdate")
				uBalance = request.POST.get("Balance")
				uCreditScore = request.POST.get("Credit_Score")
				uAddressCity = request.POST.get("Address_City")
				uAddressStreet = request.POST.get("Address_Street")
				uAddressProvince = request.POST.get("Address_Province")

				form = User(
					First_Name = uFname, 
					Last_Name = uLname, 
					Mobile_Number = uMobile, 
					Email = uEmail, 
					Password = uPassword, 
					Birthdate = uBirthdate, 
					Balance = uBalance, 
					Credit_Score = uCreditScore, 
					Address_City = uAddressCity, 
					Address_Street = uAddressStreet, 
					Address_Province = uAddressProvince)
				
				form.save()
				return redirect('http://127.0.0.1:8000/admindashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR ADD BANK
	def AddBank(request):
		if request.method == "POST":
			form = BankForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#PRIMARY BANK ATTRIBUTES
				bAccount_Number = request.POST.get("Account_Number")
				bBalance = request.POST.get("Balance")
				bBank_Info_ID = request.POST.get("Bank_Info_ID")

				form = Bank(
					Account_Number = bAccount_Number,
					Balance = bBalance,
					Bank_Info_ID = BankInfo.objects.get(Bank_Info_ID = bBank_Info_ID)
				)
				
				form.save()
				return redirect('http://127.0.0.1:8000/admindashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR ADD BANK INFO
	def AddBankInfo(request):
		if request.method == "POST":
			form = BankInfoForm(request.POST)
		

			if form.is_valid():
				print(form.is_valid())
				#PRIMARY BANK ATTRIBUTES
				bankInfoBank = request.POST.get("Bank")
				bankInfoUser = request.POST.get("User_ID")
				#print(bankInfoUser)

				form = BankInfo(
					Bank = bankInfoBank,
					User_ID = User.objects.get(User_ID = bankInfoUser)
				)
				
				form.save()
				return redirect('http://127.0.0.1:8000/admindashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR ADD FEEDBACK
	def AddFeedback(request):
		if request.method == "POST":
			form = FeedbackForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#PRIMARY BANK ATTRIBUTES
				feedbackReciever = request.POST.get("Receiver_ID")
				feedbackSender = request.POST.get("Sender_ID")
				feedbackMessage = request.POST.get("Message")
				#print(bankInfoUser)

				form = Feedback(
					Receiver_ID = User.objects.get(User_ID = feedbackReciever),
					Sender_ID = User.objects.get(User_ID = feedbackSender),
					Message = feedbackMessage
				)
				
				form.save()
				return redirect('http://127.0.0.1:8000/admindashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR ADD TRANSACTIONS
	def AddTransaction(request):
		if request.method == "POST":
			form = TransactionForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#PRIMARY BANK ATTRIBUTES
				transLender = request.POST.get("Lender_ID")
				transBorrower = request.POST.get("Borrower_ID")
				transAmount = request.POST.get("Amount")
				transIR = request.POST.get("Interest_Rate")
				transTD = request.POST.get("Transaction_Date")
				transDD = request.POST.get("Date_Due")
				transDP = request.POST.get("Date_Paid")
				transStatus = request.POST.get("Status")
				#print(bankInfoUser)

				form = Transaction(
					Lender_ID = User.objects.get(User_ID = transLender),
					Borrower_ID = User.objects.get(User_ID = transBorrower),
					Amount = transAmount,
					Interest_Rate = transIR,
					Transaction_Date = transTD,
					Date_Due = transDD,
					Date_Paid = transDP,
					Status = transStatus

				)
				
				form.save()
				return redirect('http://127.0.0.1:8000/admindashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR ADD MESSAGE
	def AddMessage(request):
		if request.method == "POST":
			form = MessageForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#PRIMARY MESSAGE ATTRIBUTES
				msgTransID = request.POST.get("Transaction_ID")
				msgTimeSent = request.POST.get("Time_Sent")
				msgDateSent = request.POST.get("Date_Sent")
				msg = request.POST.get("Message")
				msgSendID = request.POST.get("Sender_ID")

				form = Message(
					Transaction_ID = Transaction.objects.get(Transaction_ID = msgTransID),
					Time_Sent = msgTimeSent,
					Date_Sent = msgDateSent,
					Message = msg,
					Sender_ID = User.objects.get(User_ID = msgSendID)

				)

				form.save()
				return redirect('http://127.0.0.1:8000/admindashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')


	#UPDATE FUNCTIONS

	#FOR USER
	def UpdateUser(request):
		if request.method == "POST":
			usID = request.POST.get("User_ID")
			usFname = request.POST.get("First_Name")
			usLname = request.POST.get("Last_Name")
			usMobileNumber = request.POST.get("Mobile_Number")
			usEmail = request.POST.get("Email")
			usPassword = request.POST.get("Password")
			usBirthdate = request.POST.get("Birthdate")
			usBalance = request.POST.get("Balance")
			usCS = request.POST.get("Credit_Score")
			usAddressCity = request.POST.get("Address_City")
			usAddressStreet = request.POST.get("Address_Street")
			usAddressProvince = request.POST.get("Address_Province")

			User.objects.filter(User_ID = usID).update(
				First_Name = usFname, 
				Last_Name = usLname, 
				Mobile_Number = usMobileNumber, 
				Email = usEmail, 
				Password = usPassword, 
				Birthdate = usBirthdate, 
				Balance = usBalance, 
				Credit_Score = usCS, 
				Address_City = usAddressCity, 
				Address_Street = usAddressStreet, 
				Address_Province = usAddressProvince)

			return redirect('http://127.0.0.1:8000/admindashboard/')

	#FOR BANK
	def UpdateBank(request):
		if request.method == "POST":
			bankID = request.POST.get("Bank_ID")
			bankAccNumber = request.POST.get("Account_Number")
			bankBalance = request.POST.get("Balance")

			Bank.objects.filter(Bank_ID = bankID).update(
				Account_Number = bankAccNumber, 
				Balance = bankBalance)

			return redirect('http://127.0.0.1:8000/admindashboard/')

	#FOR BANK INFO
	def UpdateBankInfo(request):
		if request.method == "POST":
			bankInfoID = request.POST.get("Bank_Info_ID")
			bankInfoBank = request.POST.get("Bank")

			BankInfo.objects.filter(Bank_Info_ID = bankInfoID).update(
				Bank = bankInfoBank)

			return redirect('http://127.0.0.1:8000/admindashboard/')

	#FOR FEEDBACK
	def UpdateFeedback(request):
		if request.method == "POST":
			feedbackID = request.POST.get("Feedback_ID")
			feedbackMessage = request.POST.get("Message")

			Feedback.objects.filter(Feedback_ID = feedbackID).update(
				Message = feedbackMessage)

			return redirect('http://127.0.0.1:8000/admindashboard/')

	#FOR TRANSACTION
	def UpdateTransaction(request):
		if request.method == "POST":
			transID = request.POST.get("Transaction_ID")
			transAmount = request.POST.get("Amount")
			transInterRate = request.POST.get("Interest_Rate")
			transDateDue = request.POST.get("Date_Due")
			transDate = request.POST.get("Transaction_Date")
			transStatus = request.POST.get("Status")
			transDatePaid = request.POST.get("Date_Paid")

			Transaction.objects.filter(Transaction_ID = transID).update(
				Amount = transAmount, 
				Interest_Rate = transInterRate, 
				Date_Due = transDateDue, 
				Transaction_Date = transDate, 
				Status = transStatus, 
				Date_Paid = transDatePaid)

			return redirect('http://127.0.0.1:8000/admindashboard/')

	#FOR MESSAGE
	def UpdateMessage(request):
		if request.method == "POST":
			msgID = request.POST.get("Message_ID")
			msgTimeSent = request.POST.get("Time_Sent")
			msgDateSent = request.POST.get("Date_Sent")
			msg = request.POST.get("Message")

			Message.objects.filter(Message_ID = msgID).update(
				Time_Sent = msgTimeSent, 
				Date_Sent = msgDateSent, 
				Message = msg)
			
			return redirect('http://127.0.0.1:8000/admindashboard/')



	#DELETE FUNCTIONS
	#FOR USER
	def DeleteUser(request):
		if request.method == "POST":
			usID = request.POST.get("User_ID")
			User.objects.filter(User_ID = usID).delete()
			return redirect('http://127.0.0.1:8000/admindashboard/')


	#FOR BANK
	def DeleteBank(request):
		if request.method == "POST":
			bankID = request.POST.get("Bank_ID")
			Bank.objects.filter(Bank_ID = bankID).delete()
			return redirect('http://127.0.0.1:8000/admindashboard/')


	#FOR BANK INFO
	def DeleteBankInfo(request):
		if request.method == "POST":
			bankInfoID = request.POST.get("Bank_Info_ID")
			BankInfo.objects.filter(Bank_Info_ID = bankInfoID).delete()
			return redirect('http://127.0.0.1:8000/admindashboard/')


	#FOR FEEDBACK
	def DeleteFeedback(request):
		if request.method == "POST":
			feedbackID = request.POST.get("Feedback_ID")
			Feedback.objects.filter(Feedback_ID = feedbackID).delete()
			return redirect('http://127.0.0.1:8000/admindashboard/')


	#FOR TRANSACTION
	def DeleteTransactions(request):
		if request.method == "POST":
			transID = request.POST.get("Transaction_ID")
			Transaction.objects.filter(Transaction_ID = transID).delete()
			return redirect('http://127.0.0.1:8000/admindashboard/')


	#FOR MESSAGE
	def DeleteMessage(request):
		if request.method == "POST":
			msgID = request.POST.get("Message_ID")
			Message.objects.filter(Message_ID = msgID).delete()
			return redirect('http://127.0.0.1:8000/admindashboard/')



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

	def Withdraw(request):
			if request.method == "POST":
				user = request.session['User_ID']
				userID = User.objects.get(User_ID = user)

				bank = request.POST.get("Bank_ID")
				amount = request.POST.get("Amount")

				withdrawBank = Bank.objects.get(Bank_ID = bank)
				withdrawAmount = float(withdrawBank.Balance) - float(amount)

				Bank.objects.filter(Bank_ID = bank).update(
				Balance = withdrawAmount)

				walletAmount = float(userID.Balance) + float(amount)

				User.objects.filter(User_ID = user).update(
				Balance = walletAmount)



				return redirect('http://127.0.0.1:8000/user-profile')
			else:
				return HttpResponse('not valid')

	def Deposit(request):
			if request.method == "POST":
				user = request.session['User_ID']
				userID = User.objects.get(User_ID = user)

				bank = request.POST.get("Bank_ID")
				amount = request.POST.get("Amount")

				withdrawBank = Bank.objects.get(Bank_ID = bank)
				withdrawAmount = float(withdrawBank.Balance) + float(amount)

				Bank.objects.filter(Bank_ID = bank).update(
				Balance = withdrawAmount)

				walletAmount = float(userID.Balance) - float(amount)

				User.objects.filter(User_ID = user).update(
				Balance = walletAmount)

				return redirect('http://127.0.0.1:8000/user-profile')
			else:
				return HttpResponse('not valid')


	def PromoteUser(request):
			if request.method == "POST":
				user = request.POST.get('User_ID')
				userID = User.objects.get(User_ID = user)
				form = AdminList(User_ID = userID, Last_Accessed = datetime.datetime.now())
				form.save()
				return redirect('http://127.0.0.1:8000/admindashboard')
			else:
				return HttpResponse('not valid')

	def DemoteAdmin(request):
		if request.method == "POST":
			admin = request.POST.get("Admin_ID")
			AdminList.objects.filter(Admin_ID = admin).delete()
			return redirect('http://127.0.0.1:8000/admindashboard/')


			


				