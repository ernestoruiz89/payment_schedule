from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('payment_schedule.apps.main_app.views',
	url(r'^add/funder/$','add_funder_view', name='add_product_view'),	
	url(r'^calendario/$','schedule_table_view', name='schedule_table_view'),
)