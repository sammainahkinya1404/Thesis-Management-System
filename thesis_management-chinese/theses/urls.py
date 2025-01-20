# theses/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', thesis_list_view, name='thesis_list'),
    path('upload/', thesis_upload_view, name='thesis_upload'),
    path('review/', thesis_review_list_view, name='thesis_review_list'),
    path('feedback/<int:thesis_id>/', thesis_feedback_view, name='thesis_feedback'),
    path('progress/<int:thesis_id>/', progress_list_view, name='progress_list'),
    path('progress/<int:thesis_id>/add/', progress_add_view, name='progress_add'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('progress/<int:thesis_id>/', thesis_progress_view, name='thesis_progress'),


]
