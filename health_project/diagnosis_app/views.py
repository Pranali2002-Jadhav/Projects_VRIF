# diagnosis_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .ai_engine import AdvancedAIHealthEngine
from .models import Patient, DiagnosisRecord, LabTest
import json


# ============ WEB VIEWS ============

def diagnose(request):
    """Main diagnosis page"""
    """Main diagnosis page"""
    all_symptoms = [
        "fever", "cough", "sneezing", "runny_nose", "fatigue",
        "body_ache", "chills", "headache", "nausea", "dizziness",
        "itchy_eyes", "rash", "thirst", "dry_mouth", "dark_urine",
        "sensitivity_to_light", "shortness_of_breath", "chest_pain",
        "sore_throat", "loss_of_taste", "loss_of_smell", "vision_changes",
        "excessive_thirst", "frequent_urination", "slow_healing",
        "pale_skin", "cold_hands", "congestion",
        "severe_headache", "vomiting", "seizures", "memory_loss",
        "personality_changes", "weakness", "unexplained_weight_loss",
        "persistent_cough", "blood_in_sputum", "difficulty_swallowing",
        "blood_in_stool", "change_in_bowel_habits", "breast_lump",
        "skin_changes", "abnormal_bleeding", "abdominal_pain", "jaundice",
        "swollen_lymph_nodes", "night_sweats", "stroke_symptoms",
        "numbness", "slurred_speech", "facial_drooping", "confusion",
        "blurred_vision"
    ]

    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        gender = request.POST.get("gender")
        phone = (request.POST.get("phone") or "").strip()
        email = (request.POST.get("email") or "").strip()
        medical_history = (request.POST.get("medical_history") or "").strip()
        symptoms = request.POST.getlist("symptoms")

        # age as int (safe)
        age_raw = request.POST.get("age")
        age = int(age_raw) if age_raw and age_raw.isdigit() else None

        # Basic validation
        if not name or age is None or not gender:
            return render(request, "diagnosis_app/index.html", {
                "symptoms": all_symptoms,
                "error": "Please enter Name, Age and Gender."
            })

        # ✅ Better than get_or_create for updating fields
        patient, created = Patient.objects.update_or_create(
            name=name,
            age=age,
            gender=gender,
            defaults={
                "phone": phone,
                "email": email,
                "medical_history": medical_history
            }
        )

        # Run AI Prediction
        result = AdvancedAIHealthEngine.predict(
            symptoms_list=symptoms,
            age=age,
            gender=gender
        )

        predictions = result.get("predictions", []) or []
        top = predictions[0] if predictions else {}

        disease = top.get("disease", "Unknown")
        severity = top.get("severity", "Medium")
        urgency = top.get("urgency", "Normal")
        cure = top.get("cure", "Consult a doctor")

        diagnosis = DiagnosisRecord.objects.create(
            patient=patient,
            symptoms=", ".join(symptoms),
            predicted_diseases=json.dumps(predictions),
            primary_disease=disease,
            severity=severity,
            urgency=urgency,
            recommended_cure=cure,
            confidence_score=result.get("confidence", 0)
        )

        return render(request, "diagnosis_app/result.html", {
            "result": result,
            "diagnosis_id": diagnosis.id,
            "patient": patient
        })

    return render(request, "diagnosis_app/index.html", {"symptoms": all_symptoms})

def history(request):
    """View all diagnosis history"""
    records = DiagnosisRecord.objects.all().order_by('-created_at')
    return render(request, 'diagnosis_app/history.html', {'records': records})

def patient_detail(request, patient_id):
    """View patient details and history"""
    patient = get_object_or_404(Patient, id=patient_id)
    diagnoses = patient.diagnoses.all()
    return render(request, 'diagnosis_app/patient_detail.html', {
        'patient': patient,
        'diagnoses': diagnoses
    })


def api_docs(request):
    """API Documentation Page"""
    return render(request, 'diagnosis_app/api_docs.html')


def api_root(request):
    """API Root View - Redirects to API documentation"""
    return redirect('api_docs')


# ============ API ENDPOINTS ============

@api_view(['POST'])
@permission_classes([AllowAny])
def api_diagnose(request):
    """REST API for diagnosis"""
    try:
        data = request.data
        symptoms = data.get('symptoms', [])
        age = data.get('age')
        gender = data.get('gender')

        result = AdvancedAIHealthEngine.predict(
            symptoms_list=symptoms,
            age=int(age) if age else None,
            gender=gender
        )

        return Response({
            'success': True,
            'data': result,
            'message': 'Diagnosis completed successfully'
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_history(request):
    """REST API for diagnosis history"""
    records = DiagnosisRecord.objects.all().order_by('-created_at')[:10]
    data = []
    for record in records:
        data.append({
            'id': record.id,
            'patient': record.patient.name,
            'disease': record.primary_disease,
            'confidence': float(record.confidence_score),
            'severity': record.severity,
            'cure': record.recommended_cure,
            'date': record.created_at.strftime('%Y-%m-%d')
        })

    return Response({
        'success': True,
        'data': data,
        'count': records.count()
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_patient_list(request):
    """REST API for patient list"""
    patients = Patient.objects.all().order_by('-created_at')
    data = []
    for patient in patients:
        data.append({
            'id': patient.id,
            'name': patient.name,
            'age': patient.age,
            'gender': patient.gender,
            'phone': patient.phone,
            'email': patient.email,
            'diagnosis_count': patient.diagnoses.count(),
            'created_at': patient.created_at.strftime('%Y-%m-%d')
        })

    return Response({
        'success': True,
        'data': data,
        'count': patients.count()
    }, status=status.HTTP_200_OK)