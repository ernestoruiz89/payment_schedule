from django.shortcuts import render_to_response
from django.template import RequestContext
from payment_schedule.apps.main_app.models import funder, loan, payment
from payment_schedule.apps.home.forms import contactForm
from django.core.mail import EmailMultiAlternatives
import time
import datetime
from datetime import date, timedelta


def index_view(request):	
	def deb():
		debt = list(loan.objects.filter(status=1))
		total = 0
		for d in debt:
			total += d.principal			
		return total;
		
	def pay():
		pay = list(payment.objects.filter(status=1))
		total = 0
		for p in pay:
			total += p.amortization			
		return total;	
		
	def nextPayment():
		today = datetime.datetime.now().date()
		cerca = 0;
		index = -200
		primero = True
		nPay = list(payment.objects.all())
		nextDate = 0
		for i in nPay:	
			if(primero):
				cerca = i.payment_date.date() - today
				index = i
				primero = False
				
			if(((i.payment_date.date() - today) < cerca) and ((i.payment_date.date() >= today))):
				cerca = i.payment_date.date() - today
				index = i
		
		if((index.payment_date.date() < today)):
			return "No hay datos"
			
		return index.payment_date.date()	
		
	#Variables a ser mostradas en el html	
	difDebtPay = '{:20,.2f}'.format((deb() - pay()))
	nextPayment = nextPayment() #datetime.datetime.strptime(str(nextPayment()),"%Y-%m-%d").strftime(' %d/%m/%Y ')		
	ctx = {'difDebtPay':difDebtPay,'nextPayment' :nextPayment}

	return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def about_view(request):
	mensaje = "esto es un mensaje desde vista"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def funders_view(request):
	fnd = funder.objects.filter(status=True)
	ctx = {'funders':fnd}
	return render_to_response('home/funders.html',ctx,context_instance=RequestContext(request))

def contact_view(request):
	send_info = False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		contactform = contactForm(request.POST)
		if contactform.is_valid():
			send_info = True
			email = contactform.cleaned_data['Email']
			title = contactform.cleaned_data['Title']
			text = contactform.cleaned_data['Text']
			
			#sed message to gmail
			to_admin = "ruize.20.07@gmail.com"
			html_content = "received info from [ % ]: <br/><br/><br/>***Message***<br/><br/><br/>%s"%(email,text)
			msg = EmailMultiAlternatives('contatct email',html_content,'from@server.com', [to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		contactform = contactForm()		
	ctx = {'form':contactform,'email':email,'title':title,'text':text,'send_info':send_info}
	return render_to_response('home/contact.html',ctx,context_instance=RequestContext(request))