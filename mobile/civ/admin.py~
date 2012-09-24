from django.contrib import admin
from models import Purchase, Company, UserProfile, Administrator, Structure, PaymentMode, Product, Urgency, Investment, Comment, Affiliate

class PurchaseAdmin(admin.ModelAdmin):
	list_display=('product','name','email','phone_number','quantity','date','time')
	search_fields=('product','name','email','phone_number','quantity','date','time')
	list_filter=['product','name','email','phone_number','quantity','date','time']

class AffiliateAdmin(admin.ModelAdmin):
	list_display=('name','age','postal_address','home_address','email','phone_number','nationality','highest_academic_qualification',
			'referrer','reason_for_registering','date','time')
	search_fields=('name','age','postal_address','home_address','email','phone_number','nationality','highest_academic_qualification',
			'referrer','reason_for_registering','date','time')
	list_filter=['name','age','postal_address','home_address','email','phone_number','nationality','highest_academic_qualification',
			'referrer','reason_for_registering','date','time']

class ProductAdmin(admin.ModelAdmin):
	list_display=('structure','name')
	search_fields=('structure','name')
	list_filter=['structure','name']

class UrgencyAdmin(admin.ModelAdmin):
	list_display=['urgent']

class CompanyAdmin(admin.ModelAdmin):
	list_display=('name','location','products','payment_mode','date','phone','email','website')
	search_fields=('name','location', 'products')
	list_filter=['name', 'location', 'products']

class StructureAdmin(admin.ModelAdmin):
	list_display=('name','phone')
	search_fields=('name','phone')
	list_filter=('name','phone')

class UserProfileAdmin(admin.ModelAdmin):
	list_display=('name','phone','email')
	search_fields=('name','phone','email')
	list_filter=['phone']

class AdministratorAdmin(admin.ModelAdmin):
	list_display=('company','date','product')
	search_fields=('company','date','product')
	list_filter=['company','date','product']

class InvestmentAdmin(admin.ModelAdmin):
	list_display=('name','phone','email','structure','amount','extra_details','date','time')
	search_fields=('name','phone','email','structure','amount','extra_details','date')
	list_filter=('name','phone','email','structure','amount','extra_details','date','time')

class PaymentModeAdmin(admin.ModelAdmin):
	list_display=['payment_type']
	search_fields=['payment_type']
	list_filter=['payment_type']

class CommentAdmin(admin.ModelAdmin):
	list_display=('author','comment')
	search_fields=('author','comment')
	list_filter=('author','comment')
	
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Affiliate,AffiliateAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Administrator,AdministratorAdmin)
admin.site.register(Structure,StructureAdmin)
admin.site.register(PaymentMode,PaymentModeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Urgency,UrgencyAdmin)
admin.site.register(Investment,InvestmentAdmin)
admin.site.register(Comment,CommentAdmin)

