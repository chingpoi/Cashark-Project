from django.db import models
from django.db.models.fields.related import ForeignKey
# Create your models here.

class User(models.Model):
    User_ID = models.AutoField(auto_created = True, primary_key = True)
    First_Name = models.CharField(max_length = 50)
    Last_Name = models.CharField(max_length = 50)
    Mobile_Number = models.CharField(max_length = 15, unique = True)
    Email = models.CharField(max_length = 50, unique = True)
    Password = models.CharField(max_length = 50)
    Birthdate = models.CharField(max_length = 10)
    Balance = models.DecimalField(null = True, blank=True, max_digits=19, decimal_places=2)
    Credit_Score = models.IntegerField(null = True, blank=True, default=0)
    Address_Province = models.CharField(max_length = 50)
    Address_City = models.CharField(max_length = 50)
    Address_Street = models.CharField(max_length = 50)

    class meta:
        db_table = 'tblUser'


class BankInfo(models.Model):
    Bank_Info_ID = models.AutoField(auto_created = True, primary_key = True)
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    Bank = models.CharField(max_length = 50)

    class meta:
        db_table = 'tblBankInfo'


class Transaction(models.Model):
    Transaction_ID = models.AutoField(auto_created = True, primary_key = True)
    Lender_ID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='Lender')
    Borrower_ID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='Borrower')
    Amount = models.IntegerField()
    Interest_Rate = models.IntegerField()
    Transaction_Date = models.CharField(max_length = 10)
    Date_Due = models.CharField(max_length = 10)
    Date_Paid = models.CharField(max_length = 10, null = True, blank=True)
    Status = models.CharField(max_length = 10)

    class meta:
        db_table = 'tblTransaction'


class Message(models.Model):
    Message_ID = models.AutoField(auto_created = True, primary_key = True)
    Transaction_ID = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    Sender_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    Date_Sent = models.CharField(max_length = 10)
    Time_Sent = models.CharField(max_length = 10)
    Message = models.CharField(max_length = 200)

    class meta:
        db_table = 'tblMessage'


class Bank(models.Model):
    Bank_ID = models.AutoField(auto_created = True, primary_key = True)
    Bank_Info_ID = models.ForeignKey(BankInfo, on_delete = models.CASCADE)
    Account_Number = models.CharField(max_length = 50)
    Balance = models.DecimalField(null = True, blank=True, max_digits=19, decimal_places=2)

    class meta:
        db_table = 'tblBank'

class Feedback(models.Model):
    Feedback_ID = models.AutoField(auto_created = True, primary_key = True)
    Receiver_ID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='Receiver')
    Sender_ID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='Sender')
    Message = models.CharField(max_length = 200)

    class meta:
        db_table = 'tblFeedback'

class AdminList(models.Model):
    Admin_ID = models.AutoField(auto_created = True, primary_key = True)
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    Last_Accessed = models.CharField(max_length = 50)

    class meta:
        db_table = 'tblAdminList'