from django.contrib.gis.db import models
from constants import *

from company_tree.models import Position

		
###############################################################################################################################
		
class Compensation(models.Model):
	position	=	models.ForeignKey("company_tree.Position", )
	
	benefits	=	models.TextField(blank=True)
	perdiem		=	models.TextField("Per Diem", blank=True)
	
	training_pay	=	models.IntegerField(choices=PAY_TYPE, default=0)
	training_contract=	models.BooleanField(default=False)

	extra_info	=	models.TextField(blank=True)
	last_modified	=	models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return "comp: %s" % self.position
		
		
class PayscaleYear(models.Model):
	compensation	=	models.ForeignKey("Compensation", )
	year		=	models.IntegerField()
	amount		=	models.FloatField()
	salary_unit	=	models.IntegerField(choices=SALARY_TYPE)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.compensation.position, self.year)
