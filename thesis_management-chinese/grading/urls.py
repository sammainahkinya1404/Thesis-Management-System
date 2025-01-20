# grading/urls.py
from django.urls import path
from .views import grade_list_view, grade_thesis_view

urlpatterns = [
    path('', grade_list_view, name='grade_list'),
    path('<int:thesis_id>/', grade_thesis_view, name='grade_thesis'),
]
