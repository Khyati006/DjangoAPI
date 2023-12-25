# creating the serilizer. Serilizer helps to convert the object into the JSON.
from rest_framework import serializers
from api.models import Company,Employee
class companySerilizer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerilizer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"

