from django.contrib import admin
from django.urls import path,include
from api.views import Companyviewset,EmployeeViewset
from rest_framework import routers
# here we will register the viewset with routers
router=routers.DefaultRouter()
router.register(r'companies',Companyviewset)
router.register(r'employee',EmployeeViewset)

urlpatterns = [

    path('',include(router.urls))

]