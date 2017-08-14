from rest_framework import serializers
from student_app.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = '__all__'
#
# class ExamSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Exam
#         fields = '__all__'