from django import forms
from django.contrib.auth.models import User
from .models import Teacher, Subject

class TeacherRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())

    class Meta:
        model = Teacher
        fields = ['subject']

    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        teacher = Teacher.objects.create(user=user, subject=self.cleaned_data['subject'])
        return teacher
