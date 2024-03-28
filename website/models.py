from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

class TranRec(models.Model):
	date     = models.DateField()
	material = models.CharField(max_length=50)
	quantity = models.BigIntegerField()
	price    = models.BigIntegerField()
	
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
		
class Product(models.Model):
	product  = models.BigIntegerField(primary_key=True)
	prodes   = models.CharField(max_length=50)
	
	def __str__(self):
		return (f"{self.product}")
	
class Customer(models.Model):
	customer = models.BigIntegerField(primary_key=True, )
	cusdes   = models.CharField(max_length=50)
	
	def __str__(self):
		return (f"{self.customer}")
	
class TranSacRec(models.Model):
	date     = models.DateField()
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	product  = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.BigIntegerField()
	price    = models.BigIntegerField()
	totamt   = models.BigIntegerField()
	
	def __str__(self):
		return (f"{self.customer}")