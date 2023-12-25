from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serilizers import companySerilizer,EmployeeSerilizer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class Companyviewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=companySerilizer

    # this is link between employee and company
    # api/v1/company_id/employee-->this url will get the all employee of particular company
    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serilizer=EmployeeSerilizer(emps,many=True,context={'request':request})
            return Response(emps_serilizer.data)
        except Exception as e:
            print(e)


class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerilizer

