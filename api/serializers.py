from rest_framework import serializers
from .models import employee


class EmployeeSerializers(serializers.ModelSerializer):
      class Meta:
            model=employee
            fields="__all__"
class EmployeeUpdateSerializers(serializers.ModelSerializer):
      class Meta:
            model=employee
            fields=["FirstName","LastName","Mobno","Gender","DOB","address","Department","Designation","AadharNumber","ProfileImage","AadharImage"]
class AdminSerializers(serializers.ModelSerializer):
      class Meta:
            model=employee 
            fields=['uname','password','email']