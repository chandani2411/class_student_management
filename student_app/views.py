from django.shortcuts import render
from student_app.models import *
from rest_framework import viewsets
from student_app.serializers import *
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @list_route(methods=(['GET']))
    def search_student_by_roll_no(self,request):
        queryset=Student.objects.all()
        roll_number=request.query_params.get("roll_no")
        queryset=queryset.get(roll_no=roll_number)
        student_info=StudentSerializer(queryset)
        return Response(student_info.data)

    @list_route(methods=(['GET']))
    def search_students_by_subject(self,request):
        queryset = Student.objects.all()
        sub_code = request.query_params.get("sub_code")
        queryset = queryset.filter(subject__sub_code=sub_code)
        print(queryset)
        student_info = StudentSerializer(queryset,many=True)
        print(student_info.data)
        return Response(student_info.data)


