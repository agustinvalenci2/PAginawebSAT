from django.contrib import admin
from .models import	*
Classes=[Profesionprofile,Category,Consulanteducation,
		Consultant,Consultantreference,Consultantskill,
		Education,Educationinstitution,
		Reference,Skill,Workexperience]
for c in Classes:
	admin.site.register(c)


