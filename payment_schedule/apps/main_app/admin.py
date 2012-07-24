from django.contrib import admin

from payment_schedule.apps.main_app.models import country, frequency, funder, loan, payment

admin.site.register(country)
admin.site.register(frequency)
admin.site.register(funder)
admin.site.register(loan)
admin.site.register(payment)
