from django.db import models
from datetime import datetime

class pais(models.Model):
	pais 			= models.CharField(unique=True, max_length=200)
	status 			= models.BooleanField(default=True)	
	def __unicode__(self):		
		return self.pais

class frecuencia(models.Model):
	description		= models.CharField(max_length=200,unique=True)
	def __unicode__(self):		
		return self.description
	
class inversor(models.Model):
	inversor		= models.CharField(unique=True, max_length=200)
	pais			= models.ForeignKey(pais)
	estado			= models.BooleanField(default=True)
	def __unicode__(self):		
		return self.name

class financiamiento(models.Model):
	inversor     	= models.ForeignKey(inversor)
	principal   	= models.DecimalField(max_digits=19, decimal_places=2)
	plazo			= models.IntegerField()
	interest		= models.DecimalField(max_digits=19, decimal_places=2)
	frecuencia	 	= models.ForeignKey(frecuencia)	
	recibido_el  	= models.DateTimeField('Fecha recibido')
	estado			= models.BooleanField(default=True)
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



