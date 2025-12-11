from django.shortcuts import render
from rest_framework import generics, status
from .models import Employees
from .serializers import employeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from userAuth.pagination import CustomPagination
from .filter import EmplyeeFilter


class EmployeeOperation(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = employeeSerializer
    filterset_class = EmplyeeFilter
    