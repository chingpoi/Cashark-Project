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
		feedback = Feedback.objects.all()
	
		context = {
			'user': user,
			'bankInfo': bankInfo,
			'transaction': transaction,
			'message': message,
			'bank': bank,
			'feedback': feedback,
		}
		return render(request,'userdash.html',context)

	#FOR UPDATE AND DELETE FUNCTIONS/METHODS
	def post(self, request):
		if request.method == 'POST':
			#FOR USER
			if 'btnUpdateUser' in request.POST:
				print('User Update Button has been Clicked')
				usID = request.POST.get("User_ID")
				usFname = request.POST.get("First_Name")
				usLname = request.POST.get("Last_Name")
				usMobileNumber = request.POST.get("Mobile_Number")
				usEmail = request.POST.get("Email")
				usPassword = request.POST.get("Password")
				usBirthdate = request.POST.get("Birthdate")
				usBalance = request.POST.get("Balance")
				usCS = request.POST.get("Credit_Score")

				update_user = User.objects.filter(User_ID = usID).update(
					First_Name = usFname, Last_Name = usLname, Mobile_Number = usMobileNumber, Email = usEmail, Password = usPassword, Birthdate = usBirthdate, Balance = usBalance, Credit_Score = usCS)

				print(update_user)
				print('User Updated! Yey!')
				return redirect('http://127.0.0.1:8000/admindashboard/')
			elif 'btnDeleteUser' in request.POST:
				print('User Delete Button has been Clicked')
				usID = request.POST.get("User_ID")
				User.objects.filter(User_ID = usID).delete()
				print('USER Record Deleted')
				return redirect('http://127.0.0.1:8000/admindashboard/')

			#FOR BANK
			elif 'btnUpdateBank' in request.POST:
				print('Bank Update Button has been Clicked')
				bankID = request.POST.get("Bank_ID")
				bankAccNumber = request.POST.get("Account_Number")
				bankBalance = request.POST.get("Balance")

				update_bank = Bank.objects.filter(Bank_ID = bankID).update(
					Account_Number = bankAccNumber, Balance = bankBalance
				)

				print(update_bank)
				print('BANK UPDATED! YEYY!!')
				return redirect('http://127.0.0.1:8000/admindashboard/')
			elif 'btnDeleteBank' in request.POST:
				print('Bank Delete Button has been clicked')
				bankID = request.POST.get("Bank_ID")
				Bank.objects.filter(Bank_ID = bankID).delete()
				print('BANK Record Deleted')
				return redirect('http://127.0.0.1:8000/admindashboard/')

			#FOR BANK INFO
			elif 'btnUpdateBankInfo' in request.POST:
				print('Bank Info Update Button has been Clicked')
				bankInfoID = request.POST.get("Bank_Info_ID")
				bankInfoBank = request.POST.get("Bank")

				update_BankInfo = BankInfo.objects.filter(Bank_Info_ID = bankInfoID).update(Bank = bankInfoBank)

				print(update_BankInfo)
				print('Bank Info UPDATED! NOICE!')
				return redirect('http://127.0.0.1:8000/admindashboard/')
			elif 'btnDeleteBankInfo' in request.POST:
				print('Bank Info Delete Button has been clicked')
				bankInfoID = request.POST.get("Bank_Info_ID")
				BankInfo.objects.filter(Bank_Info_ID = bankInfoID).delete()
				print('BANK Info Record Deleted')
				return redirect('http://127.0.0.1:8000/admindashboard/')

			#FOR FEEDBACK
			elif 'btnUpdateFeedback' in request.POST:
				print('Feedbank Update Button has been Clicked')
				feedbackID = request.POST.get("Feedback_ID")
				feedbackMessage = request.POST.get("Message")

				update_Feedback = Feedback.objects.filter(Feedback_ID = feedbackID).update(Message = feedbackMessage)

				print(update_Feedback)
				print('Feedback UPDATED! NOIIIICEEEEE!')
				return redirect('http://127.0.0.1:8000/admindashboard/')
			elif 'btnDeleteFeedback' in request.POST:
				print('Feedback Delete Button has been clicked')
				feedbackID = request.POST.get("Feedback_ID")
				Feedback.objects.filter(Feedback_ID = feedbackID).delete()
				print('FEEDBACK Record Deleted')
				return redirect('http://127.0.0.1:8000/admindashboard/')

			#FOR TRANSACTIONS
			elif 'btnUpdateTransactions' in request.POST:
				print('Transactions Update Button has been Clicked')
				transID = request.POST.get("Transaction_ID")
				transAmount = request.POST.get("Amount")
				transInterRate = request.POST.get("Interest_Rate")
				transDateDue = request.POST.get("Date_Due")
				transDate = request.POST.get("Transaction_Date")
				transStatus = request.POST.get("Status")
				transDatePaid = request.POST.get("Date_Paid")

				update_Transactions = Transaction.objects.filter(Transaction_ID = transID).update(
					Amount = transAmount, Interest_Rate = transInterRate, Date_Due = transDateDue, Transaction_Date = transDate, Status = transStatus, Date_Paid = transDatePaid
				)

				print(update_Transactions)
				print('Transactions UPDATED! LEZGO!')
				return redirect('http://127.0.0.1:8000/admindashboard/')
			elif 'btnDeleteTransactions' in request.POST:
				print('Transactions Delete Button has been clicked')
				transID = request.POST.get("Transaction_ID")
				Transaction.objects.filter(Transaction_ID = transID).delete()
				print('TRANSACTION Record Deleted')
				return redirect('http://127.0.0.1:8000/admindashboard/')

			#FOR MESSAGE
			elif 'btnUpdateMessage' in request.POST:
				print('Message Update Button has been Clicked')
				msgID = request.POST.get("Message_ID")
				msgTimeSent = request.POST.get("Time_Sent")
				msgDateSent = request.POST.get("Date_Sent")
				msg = request.POST.get("Message")

				update_Message = Message.objects.filter(Message_ID = msgID).update(
					Time_Sent = msgTimeSent, Date_Sent = msgDateSent, Message = msg
				)

				print(update_Message)
				print('Message UPDATED! SHEESHH!')
				return redirect('http://127.0.0.1:8000/admindashboard/')
			elif 'btnDeleteMessage' in request.POST:
				print('Message Delete Button has been clicked')
				msgID = request.POST.get("Message_ID")
				Message.objects.filter(Message_ID = msgID).delete()
				print('MESSAGE Record Deleted')
				return redirect('http://127.0.0.1:8000/admindashboard/')


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


				