# Create your views here.

from django.http import *

def merhaba_dunya(request):
    return HttpResponse(u'<h1>Tugba Dal </h1> Merhaba ben Tugba Dal')