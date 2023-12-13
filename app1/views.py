from django.shortcuts import render
from app1.models import *
# Create your views here.
def depttable(request):
    dto=dept.objects.all()
    d={'dept':dto}
    return render(request,'depttable.html',d)


def emptable(request):
    eto=emp.objects.all()
    d={'emp':eto}
    return render(request,'emptable.html',d)