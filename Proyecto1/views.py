from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
import random	 
def saludo(request):
	plt=get_template("plantilla1.html")
	

	ctx={'name':random.random}
	documento=plt.render(ctx)
	return HttpResponse	(documento)
