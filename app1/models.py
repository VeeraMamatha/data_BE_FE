from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField()
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.dname

class emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    mgr=models.IntegerField()
    hiredate=models.DateField()
    comm=models.IntegerField()
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

