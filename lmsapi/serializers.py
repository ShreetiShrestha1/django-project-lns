from rest_framework import serializers
from core.models import Teacher, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email', 'department', 'phone_no', 'join_date','user']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'semester', 'phone_no',]