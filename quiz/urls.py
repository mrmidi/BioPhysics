from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('study/', views.study_mode, name='study_mode'),
    path('study/<int:question_id>/', views.study_mode, name='study_mode_question'),
    path('check_answer/<int:question_id>/', views.check_answer, name='check_answer'),
]
