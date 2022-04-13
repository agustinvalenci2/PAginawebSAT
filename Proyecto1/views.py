from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
import random
from .models import *
def createUser(request):
	cdict=dict()
	for g in request.session['general']:
		print(request.session['general'][g])
	C=dict()
	C['general']=['phone','email','firstname','lastname','country','state','city','citizenship','birthday','skype','facebook','linkedin']
	C['professional']=['professional_id','industry','role','experience_years','description','type_of_job','remote_experience','rate']
	C['work']=['role','company','start_date','end_date',]
	C['skills']=['skill_id', 'name', 'domain_level', 'cathegoric_level']
	C['reference']=[]
	for k in sorted(C.keys()):
		cdict=dict()
		for d in C[k]:
			cdict[d]=request.session[k].get(d)
		if k=='general':
			cdict['professional_id']=T2TProfesionprofile.objects.count()+1
			T2TConsultant.objects.create(**dict(cdict))
		elif k== 'professional':
			cdict['professional_id']=T2TProfesionprofile.objects.count()+1
			T2Tconsultant.objects.create(**dict(cdict))
		elif k=='work':
			cdict['work_id']=T2TSkill.objects.count()+1
			cdict['professional_id']=T2TProfesionprofile.objects.count()
			T2TWorkExperience.create(**dict(cdict))
		elif k=='skills':
			cdict['professional_id']=T2TProfesionprofile.objects.count()+1
			T2TSkill.create(**dict(cdict))
			T2tConsultantSkill.create(skill_id=cdict['skill_id'],professional_id=cdict['professional_id'])

def general(request):
	ctx={'name':random.random}
	documento="general.html"
	request.session['general']=dict()
	for d in request.GET.keys():
		
		request.session['general'][d]=request.GET[d]

	return render(request,documento)	 
def professional(request):
	request.session['professional']=dict()
	for d in request.GET.keys():
		
		request.session['professional'][d]=request.GET[d]

	ctx={'name':random.random}
	documento="professional.html"
	return render(request,documento)	
def languages(request):
	request.session['languages']=dict()
	for d in request.GET.keys():
		
		request.session['languages'][d]=request.GET[d]

	
	ctx={'name':random.random}
	documento="languages.html"
	return render(request,documento)	
def skills(request):
	request.session['skills']=dict()
	for d in request.GET.keys():
		
		request.session['skills'][d]=request.GET[d]

	ctx={'name':random.random}
	documento="skills.html"
	return render(request,documento)	
def work(request):
	request.session['work']=dict()
	for d in request.GET.keys():
		
		request.session['work'][d]=request.GET[d]

	ctx={'name':random.random}
	documento="work.html"
	return render(request,documento)	

def reference(request):
	request.session['reference']=dict()
	for d in request.GET.keys():
		
		request.session['reference'][d]=request.GET[d]

	ctx={'name':random.random}
	print(dict(request.session))
	#createUser(request)
	documento="reference.html"
	return render(request,documento)	

def education(request):
	request.session['education']=dict()
	for d in request.GET.keys():
		
		request.session['education'][d]=request.GET[d]

	ctx={'name':random.random}
	documento="education.html"
	return render(request,documento)	