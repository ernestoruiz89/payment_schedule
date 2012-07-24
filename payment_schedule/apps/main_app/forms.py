from django import forms
from payment_schedule.apps.main_app.models import country

class addFunderForm(forms.Form):
	Name = forms.CharField(widget=forms.TextInput())
	Country = forms.ModelChoiceField(
		queryset = country.objects.all()
	)
	
	def clean(self):
		return self.cleaned_data