from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employees
from .serializers import EmployeesSerializer

class EmployeeList(APIView):

    def get(self,request):
        employee1 = Employees.objects.all()
        serializer = EmployeesSerializer(employee1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
