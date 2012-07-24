from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('payment_schedule.apps.home.views',
	url(r'^$','index_view', name='main_view'),
	url(r'^about/$','about_view', name='about_view'),
	url(r'^funders/$','funders_view', name='funders_view'),
	url(r'^contact/$','contact_view', name='contact_view'),
)