from django import forms

class contactForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Title = forms.CharField(widget=forms.TextInput())
	Text = forms.CharField(widget=forms.Textarea())