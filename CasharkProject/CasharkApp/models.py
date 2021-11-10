from django.db import models
from django.db.models.fields.related import ForeignKey
# Create your models here.

class User(models.Model):
    User_ID = models.AutoField(auto_created = True, primary_key = True)
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 50)
    
    class meta:
        db_table = 'tblUser'