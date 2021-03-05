from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer
