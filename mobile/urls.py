from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'civ.views.home', name='home'),
	# url(r'^civ/', include('civ.foo.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	url(r'^mobile/', include('mobile.civ.urls')),
	#url(r'^reg/', include('mobile.regtr.urls')),
)
