# diagnosis_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Web Views
    path('', views.diagnose, name='diagnose'),
    path('history/', views.history, name='history'),
    path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('api-docs/', views.api_docs, name='api_docs'),
    path('api/', views.api_root, name='api_root'),

    # API Endpoints
    path('api/diagnose/', views.api_diagnose, name='api_diagnose'),
    path('api/history/', views.api_history, name='api_history'),
    path('api/patients/', views.api_patient_list, name='api_patient_list'),
]