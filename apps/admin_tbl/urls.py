from django.urls import path
from . import views


app_name= "admin_tbl"
urlpatterns = [
    path("", views.StudentListView.as_view(), name="student_list"),
    path("detail/<int:pk>", views.StudentDetail.as_view(), name="student_detail"),
    path("create", views.StudentCreate.as_view(), name="student_create"),
    path("update/<int:pk>", views.StudentUpdate.as_view(), name="student_update"),
    path("delete/<int:pk>", views.StudentDelete.as_view(), name="student_delete"),
]
