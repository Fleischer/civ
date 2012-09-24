from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'mobile.civ.views.home'),
	url(r'^list/$', 'mobile.civ.views.structure_list'),
	url(r'^product-(detail|info)/(?P<id>\d+)$', 'mobile.civ.views.product_detail'),
	url(r'^purchase/(?P<id>\d+)?$', 'mobile.civ.views.purchase_prod'),
	url(r'^affiliate/(?P<id>\d+)?$', 'mobile.civ.views.affiliate'),
	url(r'^structure/(?P<id>\d+)?$', 'mobile.civ.views.structure_detail'),
	url(r'^contact_us/$', 'mobile.civ.views.contact_us'),
	url(r'^invest/$', 'mobile.civ.views.contact_civ'),
	url(r'^confirm/(?P<id>\d+)?$', 'mobile.civ.views.company_confirm'),
	url(r'^invest_confirm/(?P<id>\d+)?$', 'mobile.civ.views.invest_confirm'),
	url(r'^about_us/$', 'mobile.civ.views.about_us'),
	url(r'^comment/$', 'mobile.civ.views.comment_list'),
	url(r'^post_comment/$', 'mobile.civ.views.post_comment'),
	url(r'^edit_comment/(?P<id>\d+)?$', 'mobile.civ.views.edit_comment'),
	url(r'^search/(.*)$', 'mobile.civ.views.search'),
	url(r'^confirmation/(?P<id>\d+)?$', 'mobile.civ.views.prod_confirm'),
#	url(r'^staff/(.*)?$', 'civ.views.park_search'),
)

