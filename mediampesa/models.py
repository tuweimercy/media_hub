from django.db import models
from django.conf import settings

# Create your models here.
class Transactions(models.Model):
    #transactions id: valid transaction id frm mpesa
    transaction_id = models.CharField(max_length=100,
    blank=True,null=True)
    #PHONE NO THAT PAID /ATTEMPTED TO PAY
    phone_number = models.CharField(max_length=15)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    #mpesa receipts
    mpesa_receipt_number = models.CharField(
        max_length=100, blank=True, null=True)
    #Status transaction(complete,pending,fail)
    status= models.CharField(max_length=50,blank=True,null=True)
    description=models.CharField(blank=True,null=True)
    transaction_date= models.DateField(auto_now_add=True)
    date_created= models.DateField(auto_now_add=True)
    email= models.EmailField(blank=True,null=True)
    name= models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f"Transaction ={self.mpesa_receipt_number}"
    
