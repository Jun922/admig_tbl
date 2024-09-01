from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .models import Student
from .forms import StudentForm


class StudentsListView(ListView):
    template_name = 'admin_tbl/student_list.html'
    model = Student
    