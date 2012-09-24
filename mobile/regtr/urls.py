from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^login/$', 'regtr.views.loginView'),
	url(r'^logout/$', 'regtr.views.logoutView'),
	url(r'^signup/$', 'regtr.views.signUpView'),
)

