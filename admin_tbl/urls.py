from django.urls import path
from . import views


app_name= 'admin_tbl'
urlpatterns = [
    path("", views.StudentsListView.as_view(), name='student_list'),
]
