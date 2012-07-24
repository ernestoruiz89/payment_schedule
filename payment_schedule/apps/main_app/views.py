from django.shortcuts import render_to_response
from django.template import RequestContext
from payment_schedule.apps.main_app.forms import addFunderForm
from payment_schedule.apps.main_app.models import funder
from datetime import datetime 

def add_funder_view(request):
	if request.method == "POST":
		form = addFunderForm(request.POST)
		info = "Init"
		if form.is_valid():
			name = form.cleaned_data['Name']
			country = form.cleaned_data['Country']
			f = funder()
			f.name = name
			f.country = country
			f.status = True
			f.created_at = datetime.now()
			f.save()
			info = "funder has been saved!!"
		else:
			info = "Incorrect data"
		form = addFunderForm()
		ctx = {'form':form, 'info':info}
		return render_to_response('schedule/addfunder.html',ctx,context_instance=RequestContext(request))
	
	else:			
		form = addFunderForm()
		ctx = {'form':form}
		return render_to_response('schedule/addfunder.html',ctx,context_instance=RequestContext(request))

