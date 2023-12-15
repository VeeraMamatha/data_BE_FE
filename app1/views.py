from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.
def depttable(request):
    dto=dept.objects.all()
    d={'dept':dto}
    return render(request,'depttable.html',d)


def emptable(request):
    eto=emp.objects.all()
    d={'emp':eto}
    return render(request,'emptable.html',d)

def insertemp(request):
    no=int(input('enter empno'))
    name=input('enter name:')
    job=input('enter job:')
    sal=int(input('enter sal:'))
    mgr=int(input('enter mgr:'))
    hiredate=input('enter hiredate:')
    comm=int(input('enter comm'))
    deptno=int(input('enter deptno:'))
    a=dept.objects.get(deptno=deptno)
    b=emp.objects.get_or_create(empno=no,ename=name,job=job,sal=sal,mgr=mgr,hiredate=hiredate,comm=comm,deptno=a)[0]
    b.save()
    return HttpResponse('EMP table is created')

def insertemp2(request):
    no=int(input('enter empno'))
    name=input('enter name:')
    job=input('enter job:')
    sal=int(input('enter sal:'))
    mgr=int(input('enter mgr:'))
    hiredate=input('enter hiredate:')
    comm=int(input('enter comm'))
    deptno=int(input('enter deptno:'))
    a=dept.objects.get(deptno=deptno)
    b=emp.objects.get_or_create(empno=no,ename=name,job=job,sal=sal,mgr=mgr,hiredate=hiredate,comm=comm,deptno=a)[0]
    b.save()
    eto=emp.objects.all()
    d={'emp':eto}
    return render(request,'emptable.html',d)