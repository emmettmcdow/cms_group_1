from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
import datetime
from uuid import uuid4

def uuid_func():
    return uuid4()

# Populate this with https://docs.djangoproject.com/en/4.0/topics/db/models/
# this is models



class Account(models.Model):
    account_number = models.CharField(max_length=30, default = uuid_func)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    account_status = models.BooleanField(default=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    transaction_type = models.CharField(max_length=6)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
# Create your models here.
