from re import S
from rest_framework import viewsets
from .models import Student
from . import serializers

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer



#list , retrieve , create , update , destroy