from django.db import models

# Create your models here.
# creating comapny and employee model

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField(max_length=500)
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non-IT','Non-IT'),('Other','Other')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True) 

    def __str__(self):
        return self.name+'-'+self.location

# we want the all the employees of particular company

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(('manager','manager'),('SDE','SDE'),('Backend Dev','Backend DEV')))
    # Relation between company and employee
    company=models.ForeignKey(Company,on_delete=models.CASCADE)


