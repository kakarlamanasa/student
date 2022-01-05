from django import forms
from studentdetails.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = '__all__'