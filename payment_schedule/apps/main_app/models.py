from django.db import models
from datetime import datetime

class country(models.Model):
	name 			= models.CharField(unique=True, max_length=200)
	status 			= models.BooleanField(default=True)	
	def __unicode__(self):		
		return self.name

class frequency(models.Model):
	description		= models.CharField(max_length=200,unique=True)
	def __unicode__(self):		
		return self.description
	
class funder(models.Model):
	name 			= models.CharField(unique=True, max_length=200)
	country			= models.ForeignKey(country)
	status			= models.BooleanField(default=True)
	created_at		= models.DateTimeField(default=datetime.now())
	def __unicode__(self):		
		return self.name

class loan(models.Model):
	funder     		= models.ForeignKey(funder)
	principal   	= models.DecimalField(max_digits=19, decimal_places=2)
	term	    	= models.IntegerField()
	interest		= models.DecimalField(max_digits=19, decimal_places=2)
	frequency	 	= models.ForeignKey(frequency)	
	received_at  	= models.DateTimeField('Received date')
	status			= models.BooleanField(default=True)
	def __unicode__(self):		
		return '%s | %s| %s'%(self.id,self.principal,self.funder.name)
	
class payment (models.Model):
	loan     		= models.ForeignKey(loan)
	amortization 	= models.DecimalField(max_digits=19, decimal_places=2)
	interest		= models.DecimalField(max_digits=19, decimal_places=2)
	payment_date	= models.DateTimeField('projected date')
	payment_at		= models.DateTimeField('Payment date')
	status			= models.BooleanField(default=False)
	def __unicode__(self):	
		fecha = self.payment_date
		dateFormat = fecha.strftime("%B %d, %Y ")
		pago = '{:20,.2f}'.format(self.amortization + self.interest)
		return 'U$ %s | %s | %s'%(pago, dateFormat, self.loan.funder.name)



