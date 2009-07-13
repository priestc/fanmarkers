# coding: UTF-8

from main.models import *
from main.constants import *

from django.http import HttpResponse
from annoying.decorators import render_to
from annoying.functions import get_object_or_None
from django.shortcuts import get_object_or_404

########################################################


@render_to('list_position.html')
def position(request):

	positions = Position.objects.all()
	
	return locals()
	
@render_to('list_aircraft-company.html')
def company(request):

	type="Company"

	from main.forms import CompanySearch
	
	objects = Company.objects.all()
	
	if request.GET:
	
		searchform = CompanySearch(request.GET)
		
		if searchform.is_valid():

			if int(searchform.cleaned_data["type"]) >= 0:
				objects = objects.filter(type=searchform.cleaned_data["type"])
		
			if int(searchform.cleaned_data["jumpseat"]) >= 0:
				objects = objects.filter(jumpseat=searchform.cleaned_data["jumpseat"])
		 
		 	if searchform.cleaned_data["search"]:
				s = searchform.cleaned_data["search"]
				objects = objects.filter( Q(name__icontains=s) | Q(description__icontains=s) )
				
	else:
		searchform = CompanySearch()

	return locals()
