from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "age", "sex", "job", "memo")
        widgets = {
                    "name": forms.TextInput(
                        attrs={
                            "class": "student-form student-name",
                            "placeholder": "記入例：山田　太郎",
                        }
                    ),
                    "age": forms.NumberInput(
                        attrs={
                            "class": "student-form student-age",
                            "min": 1,
                        }
                    ),
                    "sex": forms.RadioSelect(
                        attrs={
                            "class": "student-form student-sex",
                        }
                    ),
                    "job": forms.TextInput(
                        attrs={
                            "class": "student-form student-job",
                            "placeholder": "記入例：プログラマー",
                        }
                    ),
                    "memo": forms.Textarea(
                        attrs={
                            "class": "student-form student-memo",
                            "rows": 4,
                        }
                    ),
        }
