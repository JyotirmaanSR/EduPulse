from django import forms
from django.contrib.auth.models import User
from .models import Student, Subject

class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = ['subjects']

    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        student = Student.objects.create(user=user)
        student.subjects.set(self.cleaned_data['subjects'])
        return student
