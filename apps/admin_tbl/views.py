from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Student, Lesson
from .forms import StudentForm


# ------------------------------
#         student part
# ------------------------------
class StudentListView(ListView):
    template_name = "admin_tbl/student_list.html"
    model = Student
    context_object_name = "students"
    
    def get_queryset(self):
        queryset = Student.objects.prefetch_related("lesson")
        return queryset


class StudentDetail(DetailView):
    template_name = "admin_tbl/student_detail.html"
    model = Student
    context_object_name = "student"
    
    def get_queryset(self):
        queryset = Student.objects.prefetch_related("lesson")
        return queryset


class StudentCreate(CreateView):
    template_name = "admin_tbl/student_form.html"
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("admin_tbl:student_list")

    def get_success_url(self):
        messages.success(self.request, "記事を投稿しました。")
        return resolve_url("admin_tbl:student_list")


class StudentUpdate(UpdateView):
    template_name = "admin_tbl/student_form.html"
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse_lazy("admin_tbl:student_list")


class StudentDelete(DeleteView):
    model = Student

    def get_success_url(self):
        return reverse_lazy("admin_tbl:student_list")



# ------------------------------
#          lesson part
# ------------------------------
class LessonListView(ListView):
    template_name = "admin_tbl/lesson_list.html"
    model = Student
    context_object_name = "lessons"
    
    def get_queryset(self):
        student_id = self.kwargs['pk']
        queryset = Lesson.objects.filter(student_id=student_id).all()
        return queryset
    
    # def get_queryset(self):
    #     queryset = Student.objects.prefetch_related("lesson")
    #     return queryset


# class StudentDetail(DetailView):
#     template_name = "admin_tbl/student_detail.html"
#     model = Student
    
#     def get_queryset(self):
#         queryset = Student.objects.prefetch_related("lesson")
#         return queryset


# class StudentCreate(CreateView):
#     template_name = "admin_tbl/student_form.html"
#     model = Student
#     form_class = StudentForm
#     success_url = reverse_lazy("admin_tbl:student_list")

#     def get_success_url(self):
#         messages.success(self.request, "記事を投稿しました。")
#         return resolve_url("admin_tbl:student_list")


# class StudentUpdate(UpdateView):
#     template_name = "admin_tbl/student_form.html"
#     model = Student
#     form_class = StudentForm

#     def get_success_url(self):
#         return reverse_lazy("admin_tbl:student_list")


# class StudentDelete(DeleteView):
#     model = Student

#     def get_success_url(self):
#         return reverse_lazy("admin_tbl:student_list")
