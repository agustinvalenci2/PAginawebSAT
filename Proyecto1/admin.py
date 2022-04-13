from django.contrib import admin
from .models import	*

Classes=[T2TProfesionprofile,T2TCategory,T2TConsulanteducation,
		T2TConsultant,T2TConsultantreference,T2TConsultantskill,
		T2TEducation,T2TEducationinstitution,
		T2TReference,T2TSkill,T2TWorkexperience]

for c in Classes:
	admin.site.register(c)



