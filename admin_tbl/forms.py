from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'age', 'sex', 'job', 'memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'age': forms.NumberInput(attrs={'min':1}),
                    'sex': forms.RadioSelect(),
                    'job': forms.TextInput(attrs={'placeholder':'記入例：プログラマー'}),
                    'memo': forms.Textarea(attrs={'rows':4}),
        }