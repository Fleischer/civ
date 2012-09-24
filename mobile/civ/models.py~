from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=60)
	phone = models.CharField(max_length=40)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=60)
	structure = models.CharField(max_length=60)
	def __unicode__(self):
		return self.name

class Structure(models.Model):
	name = models.CharField(max_length=60)
	phone = models.CharField(max_length=60)
	def __unicode__(self):
		return self.name

class Urgency(models.Model):
	urgent = models.CharField(max_length=60)
	def __unicode__(self):
		return self.urgent
	
#class Date(models.Models):
#	day=models.IntegerField()
#	month=models.IntegerField()
#	year=models.IntegerField()
#	def __unicode__(self):
#		return str(self.month) +' '+ str(self.day)+', '+str(self.year)

class Purchase(models.Model):
	name = models.CharField(max_length=60, blank=True)
	email = models.EmailField(blank=True)
	phone_number = models.CharField(max_length=10, blank=True)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(null=True, blank=True)
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	def __unicode__(self):
		return self.product

class Affiliate(models.Model):
	name = models.CharField(max_length=100, blank=True)
	age = models.IntegerField(null=True, blank=True)
	postal_address = models.TextField()
	home_address = models.TextField()
	email = models.EmailField(blank=True)
	phone_number = models.CharField(max_length=15, blank=True)
	nationality = models.CharField(max_length=100, blank=True)
	highest_academic_qualification = models.CharField(max_length=100, blank=True)
	referrer = models.CharField(max_length=100, blank=True)
	reason_for_registering = models.TextField()
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	def __unicode__(self):
		return self.name

class PaymentMode(models.Model):
	payment_type = models.CharField(max_length=60)
	def __unicode__(self):
		return self.payment_type

class Comment(models.Model):
	author = models.CharField(max_length=60)
	comment = models.TextField()
#	date = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.comment

class Company(models.Model):
	name=models.CharField(max_length=60)
	location=models.CharField(max_length=100)
	payment_mode=models.ForeignKey(PaymentMode)
	products = models.TextField()
	phone=models.CharField(max_length=40)
	email=models.EmailField()
	website = models.URLField(blank=True)
	date=models.DateField(auto_now_add=True)
	def __unicode__(self):
		return self.name

class Administrator(models.Model):
	purchase = models.ForeignKey(Purchase)
	date = models.DateTimeField(auto_now=True)
	product = models.ForeignKey(Product)
	available = models.BooleanField()
	company = models.ForeignKey(Company)
	def __unicode__(self):
		return str(self.purchase) +' on '+str(self.date)

class Investment(models.Model):
	name = models.CharField(max_length=60)
	phone = models.CharField(max_length=10,blank=True)
	email = models.EmailField(blank=True)
	structure = models.ForeignKey(Structure)
	extra_details = models.TextField(blank=True)
	amount = models.FloatField(blank=True)
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)

