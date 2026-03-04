from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ])

    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    medical_history = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} (Age: {self.age})"


class DiagnosisRecord(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='diagnoses'
    )

    symptoms = models.TextField()
    test_results = models.TextField(blank=True)

    predicted_diseases = models.JSONField()

    primary_disease = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)
    urgency = models.CharField(max_length=20)

    recommended_cure = models.TextField()

    confidence_score = models.DecimalField(max_digits=5, decimal_places=2)

    ai_version = models.CharField(max_length=20, default="v2.0")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def get_symptom_list(self):
        return self.symptoms.split(", ")

    def __str__(self):
        return f"{self.patient.name} - {self.primary_disease}"


class LabTest(models.Model):
    diagnosis = models.ForeignKey(
        DiagnosisRecord,
        on_delete=models.CASCADE,
        related_name='lab_tests'
    )

    test_name = models.CharField(max_length=100)
    result_value = models.CharField(max_length=50)

    unit = models.CharField(max_length=20, blank=True)
    reference_range = models.CharField(max_length=50, blank=True)

    is_abnormal = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.test_name} - {self.result_value}"