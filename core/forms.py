from django import forms
from core.models import Teacher, Assignment, Student, Material

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'email', 'department', 'phone_no', 'join_date', 'user']
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        } 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'semester', 'phone_no', 'user']
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
       
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'start_date', 'end_date', 'question_file','question', 'full_mark', 
        'assignment_subject', 'teacher', 'remark']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            }
        
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'category', 'description', 'material_subject', 'material_file', 'upload_date', 'teacher']
        widgets = {
            'upload_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'material_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
