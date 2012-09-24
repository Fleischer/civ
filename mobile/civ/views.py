# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import User, Purchase, Company, Administrator, Product, Structure, Investment, Comment, Affiliate
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from time import mktime
import time

class SearchForm(ModelForm):
	class Meta:
		model = Structure

class PurchaseForm(ModelForm):
	class Meta:
		model = Purchase
	
class ContactForm(ModelForm):
	class Meta:
		model = Company

class InvestForm(ModelForm):
	class Meta:
		model = Investment

class CommentForm(ModelForm):
	class Meta:
		model = Comment

#Loads a list of the structures in the website
def structure_list(request):
	struc_list = Structure.objects.all()
	t = loader.get_template('civ/list.html')
	c = Context({'struc_list':struc_list, 'user':request.user.username})
	return HttpResponse(t.render(c))

#Loads a page of a structures details
def structure_detail(request, id):
	structure = Structure.objects.get(pk=id)
	products = Product.objects.filter(structure=structure.name)
	t = loader.get_template('civ/struc_detail.html')
	c = Context({'products':products,'structure':structure,'user':request.user.username})
	return HttpResponse(t.render(c))

#Loads a page of a products details
def product_detail(request, id):
	product = Product.objects.get(pk=id)
	structure = product.structure
	t = loader.get_template('civ/product.html')
	c = Context({'product':product,'structure':structure})
	return HttpResponse(t.render(c))

#Loads a purchase form and directs the customer to a confirmation page after the submit button is clicked
@csrf_exempt
def purchase_prod(request, id):
	purchases = Purchase.objects.filter()
	if request.method == 'POST':
		purchase = Purchase()
		form = PurchaseForm(request.POST, instance=purchase)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mobile/confirmation/'+str(purchase.id))
	else:
		form = PurchaseForm()
	t = loader.get_template('civ/purchase.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

#Loads an affiliate form which allows people to register as CCP Affiliates and directs them to a confirmation page after the submit button is clicked
@csrf_exempt
def affiliate(request, id):
	affiliates = Affiliate.objects.filter()
	if request.method == 'POST':
		affiliate = Affiliate()
		form = AffiliateForm(request.POST, instance=affiliate)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mobile/feedback/'+str(affiliate.id))
	else:
		form = AffiliateForm()
	t = loader.get_template('civ/affiliate.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

#Loads a confirmation page that shows the customer his or her purchase details
def prod_confirm(request, id):
	purchase = Purchase.objects.get(pk=id)
	t = loader.get_template('civ/confirm.html')
	c = Context({'name':purchase.name, 'quantity':purchase.quantity, 'date':purchase.date, 'time':purchase.time, 'product':purchase.product.name, 'email':purchase.email, 'phone':purchase.phone_number})
	return HttpResponse(t.render(c))

#Generates a form for companies, customers and investors to contact Cosmos Impact Ventures
@csrf_exempt
def contact_us(request):
	company = Company.objects.filter()
	if request.method == 'POST':
		company = Company()
		form = ContactForm(request.POST, instance=company)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mobile/confirm/'+str(company.id))
	else:
		form = ContactForm()
	t = loader.get_template('civ/register.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

#Loads a confirmation page to show companies that their company is registered
def company_confirm(request, id):
	company = Company.objects.get(pk=id)
	t = loader.get_template('civ/confirmation.html')
	c = Context({'name':company.name, 'location':company.location, 'website':company.website, 'date':company.date, 'email':company.email, 'product':company.products, 'phone':company.phone, 'payment_mode':company.payment_mode})
	return HttpResponse(t.render(c))

#Loads the CIV About Us Page
def about_us(request):
	return render_to_response("civ/about.html", {})

#Loads a page for investors of CIV
def invest_info(request):
	t = loader.get_template('civ/investor.html')
	c = Context({'name':company.name, 'location':company.location, 'website':company.website, 'date':company.date, 'email':company.email, 'product':company.products, 'phone':company.phone, 'payment_mode':company.payment_mode})
	return HttpResponse(t.render(c))

#Generates a form for investors to contact CIV
@csrf_exempt
def contact_civ(request):
	investor = Investment.objects.filter()
	if request.method == 'POST':
		invest = Investment()
		form = InvestForm(request.POST, instance=invest)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mobile/invest_confirm/'+str(invest.id))
	else:
		form = InvestForm()
	t = loader.get_template('civ/register.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

#Generates a confirmation page for the prospective investor
def invest_confirm(request, id):
	investor = Investment.objects.get(pk=id)
	t = loader.get_template('civ/invest_confirm.html')
	c = Context({'name':investor.name, 'structure':investor.structure, 'amount':investor.amount, 'date':investor.date, 'email':investor.email, 'time':investor.time, 'phone':investor.phone})
	return HttpResponse(t.render(c))

#Displays a list of customers comments
def comment_list(request):
	com_list = Comment.objects.all()
	t = loader.get_template('civ/comment.html')
	c = Context({'list':com_list})
	return HttpResponse(t.render(c))

#Generates a Comment form for customers to post comments
@csrf_exempt
def post_comment(request):
	comments = Comment.objects.filter()
	if request.method == 'POST':
		comment = Comment()
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mobile/comment')
	else:
		form = CommentForm()
	t = loader.get_template('civ/post_comment.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

#Allows customers to edit their comments
@csrf_exempt
def edit_comment(request, id):
	comment = Comment.objects.get(pk=id)
	if request.method == 'POST':
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mobile/comment')
	else:
		form = CommentForm(instance=comment)
	d = loader.get_template('civ/edit_comment.html')
	e = Context({'form':form.as_p(), 'author':comment.author, 'comment':comment.comment})
	return HttpResponse(d.render(e))

#gets data and searches through the list of structures and products
def search(request, term):
	term = request.GET.get('q', '')
	if term:
		results = Structure.objects.filter(name__icontains=term).distinct()
		products = Product.objects.filter(name__icontains=term).distinct()
	else:
		results = []
		products = []
	return render_to_response("civ/search.html", {"results": results, "products": products, "term": term,'user':request.user.username})

#Loads homepage
def home(request):
	t = loader.get_template('civ/home.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

