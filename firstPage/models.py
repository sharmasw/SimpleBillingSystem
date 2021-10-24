from django.db import models

# Create your models here.

class BillingDetail(models.Model):
    customerNumber = models.CharField(max_length=60)
    transactionID = models.IntegerField()
    timestamp = models.DateField()
    name = models.CharField(max_length=60)
    quantity = models.DecimalField(max_digits=5,decimal_places=2)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    total = models.DecimalField(max_digits=5,decimal_places=2)


class TimeStampDetails(models.Model):
    transactionID = models.IntegerField()
    transaction_date = models.DateField()
    transaction_year = models.IntegerField()
    transaction_month = models.IntegerField()
    transaction_day = models.IntegerField()
    transaction_hour = models.IntegerField()
    transaction_minute = models.IntegerField()
    transaction_week = models.IntegerField()
    transaction_weekNum = models.IntegerField()