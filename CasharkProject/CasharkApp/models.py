from django.db import models
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Address(models.Model):
    Address_ID = models.AutoField(auto_created = True, primary_key = True)
    Address_Province = models.CharField(max_length = 50)
    Address_City = models.CharField(max_length = 50)
    Address_Street = models.CharField(max_length = 50)
    
    class meta:
        db_table = 'tblAddress'


class User(models.Model):
    User_ID = models.AutoField(auto_created = True, primary_key = True)
    First_Name = models.CharField(max_length = 50)
    Last_Name = models.CharField(max_length = 50)
    Mobile_Number = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 50)
    Birthdate = models.CharField(max_length = 10)
    Address_ID = models.ForeignKey(Address, on_delete = models.CASCADE)
    Balance = models.IntegerField()
    Credit_Score = models.IntegerField()

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
    Date_Due = models.CharField(max_length = 10)
    Transaction_Date = models.CharField(max_length = 10)
    Status = models.CharField(max_length = 50)

    class meta:
        db_table = 'tblTransaction'


class Message(models.Model):
    Message_ID = models.AutoField(auto_created = True, primary_key = True)
    Transaction_ID = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    Sender = models.ForeignKey(User, on_delete = models.CASCADE)
    Time_Sent = models.CharField(max_length = 10)
    Date_Sent = models.CharField(max_length = 10)
    Message = models.CharField(max_length = 50)

    class meta:
        db_table = 'tblMessage'


class GCash(models.Model):
    Bank_Info_ID = models.ForeignKey(BankInfo, on_delete = models.CASCADE)
    Mobile_Number = models.CharField(max_length = 50)
    Balance = models.IntegerField()

    class meta:
        db_table = 'tblGCash'