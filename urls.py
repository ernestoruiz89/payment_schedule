from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('payment_schedule.apps.main_app.views',
    # Examples:
    url(r'^$', 'schedule_table_view', name='home'),
	url(r'^', include('payment_schedule.apps.home.urls')),
	url(r'^', include('payment_schedule.apps.main_app.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	
)
