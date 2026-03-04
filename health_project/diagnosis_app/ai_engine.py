# diagnosis_app/ai_engine.py

from typing import List, Dict, Any, Optional


class AdvancedAIHealthEngine:
    """AI Health Diagnosis Engine with Serious Conditions"""

    @staticmethod
    def predict(symptoms_list: List[str], age: Optional[int] = None, gender: Optional[str] = None) -> Dict[str, Any]:
        """
        Predict disease based on symptoms with improved confidence calculation
        Includes common and serious conditions
        """
        # Comprehensive symptom-disease mapping with weights
        disease_map: Dict[str, Dict[str, Any]] = {
            # ============ COMMON CONDITIONS ============
            'fever': {
                'disease': 'Flu',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Rest, drink plenty of fluids, take over-the-counter pain relievers like acetaminophen or ibuprofen. Stay hydrated and get adequate sleep.',
                'weight': 0.8
            },
            'cough': {
                'disease': 'Common Cold',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Rest, drink warm fluids, use honey for throat relief, take over-the-counter cough suppressants if needed.',
                'weight': 0.7
            },
            'headache': {
                'disease': 'Migraine',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Rest in a dark, quiet room, take pain relievers like ibuprofen or acetaminophen, stay hydrated, avoid triggers.',
                'weight': 0.6
            },
            'fatigue': {
                'disease': 'Anemia',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Iron supplements, eat iron-rich foods (spinach, red meat, beans), take vitamin C to improve absorption.',
                'weight': 0.5
            },
            'chest_pain': {
                'disease': 'Heart Attack',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'EMERGENCY: Call emergency services immediately. Do not drive yourself. Chew aspirin if not allergic. Wait for medical help.',
                'weight': 0.95
            },
            'shortness_of_breath': {
                'disease': 'Asthma',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Use prescribed inhaler, avoid triggers, take prescribed medications, see a doctor for long-term management.',
                'weight': 0.85
            },
            'excessive_thirst': {
                'disease': 'Diabetes',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Insulin therapy, monitor blood sugar, follow a healthy diet, exercise regularly, see a doctor for proper diagnosis.',
                'weight': 0.9
            },
            'frequent_urination': {
                'disease': 'UTI',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Antibiotics prescribed by doctor, drink plenty of water, avoid caffeine and alcohol, complete full course of medication.',
                'weight': 0.75
            },
            'sneezing': {
                'disease': 'Allergies',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Antihistamines, avoid allergens, use nasal sprays, keep windows closed during high pollen seasons.',
                'weight': 0.65
            },
            'body_ache': {
                'disease': 'Flu',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Rest, take pain relievers, apply warm compresses, stay hydrated, get adequate sleep.',
                'weight': 0.7
            },
            'chills': {
                'disease': 'Flu',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Rest, keep warm, drink warm fluids, take fever reducers, stay hydrated.',
                'weight': 0.75
            },
            'nausea': {
                'disease': 'Food Poisoning',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Rest, drink clear fluids, eat bland foods (BRAT diet), avoid fatty or spicy foods, stay hydrated.',
                'weight': 0.6
            },
            'dizziness': {
                'disease': 'Low Blood Pressure',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Drink water, eat small frequent meals, avoid sudden position changes, increase salt intake if recommended by doctor.',
                'weight': 0.55
            },
            'itchy_eyes': {
                'disease': 'Allergies',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Antihistamine eye drops, avoid allergens, use cold compresses, wash hands frequently.',
                'weight': 0.6
            },
            'rash': {
                'disease': 'Skin Infection',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Topical antifungal or antibiotic cream, keep area clean and dry, avoid scratching, see a doctor if it worsens.',
                'weight': 0.65
            },
            'thirst': {
                'disease': 'Dehydration',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Drink water or oral rehydration solutions, eat water-rich foods, avoid caffeine and alcohol.',
                'weight': 0.5
            },
            'dry_mouth': {
                'disease': 'Dehydration',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Drink water frequently, use sugar-free gum or lozenges, avoid caffeine and alcohol.',
                'weight': 0.55
            },
            'dark_urine': {
                'disease': 'Dehydration',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Drink more water, monitor urine color, avoid diuretics, see a doctor if it persists.',
                'weight': 0.6
            },
            'sensitivity_to_light': {
                'disease': 'Migraine',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Rest in a dark room, take pain relievers, avoid screens, wear sunglasses if needed.',
                'weight': 0.7
            },
            'sore_throat': {
                'disease': 'Strep Throat',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Antibiotics if bacterial, gargle with warm salt water, drink warm fluids, rest your voice.',
                'weight': 0.7
            },
            'loss_of_taste': {
                'disease': 'COVID-19',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Rest, isolate if positive, monitor symptoms, see a doctor if symptoms worsen, get tested.',
                'weight': 0.85
            },
            'loss_of_smell': {
                'disease': 'COVID-19',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Rest, isolate if positive, monitor symptoms, see a doctor if symptoms worsen, get tested.',
                'weight': 0.85
            },
            'vision_changes': {
                'disease': 'Eye Infection',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Eye drops prescribed by doctor, avoid contact lenses, rest eyes, see an ophthalmologist.',
                'weight': 0.7
            },
            'slow_healing': {
                'disease': 'Diabetes',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Insulin therapy, monitor blood sugar, keep wounds clean, see a doctor for proper management.',
                'weight': 0.75
            },
            'pale_skin': {
                'disease': 'Anemia',
                'severity': 'Medium',
                'urgency': 'Normal',
                'cure': 'Iron supplements, eat iron-rich foods, take vitamin C, see a doctor for proper diagnosis.',
                'weight': 0.65
            },
            'cold_hands': {
                'disease': 'Poor Circulation',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Exercise regularly, keep warm, avoid smoking, improve circulation through diet and lifestyle changes.',
                'weight': 0.5
            },
            'congestion': {
                'disease': 'Common Cold',
                'severity': 'Low',
                'urgency': 'Normal',
                'cure': 'Use decongestants, steam inhalation, drink warm fluids, rest, use a humidifier.',
                'weight': 0.7
            },

            # ============ SERIOUS CONDITIONS ============
            'severe_headache': {
                'disease': 'Brain Tumor',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'EMERGENCY: See a neurologist immediately. MRI/CT scan required. Treatment may include surgery, radiation therapy, or chemotherapy depending on tumor type and location.',
                'weight': 0.95
            },
            'vomiting': {
                'disease': 'Brain Tumor',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'EMERGENCY: See a neurologist immediately. MRI/CT scan required. Treatment may include surgery, radiation therapy, or chemotherapy depending on tumor type and location.',
                'weight': 0.9
            },
            'seizures': {
                'disease': 'Brain Tumor',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'EMERGENCY: See a neurologist immediately. MRI/CT scan required. Treatment may include surgery, radiation therapy, or chemotherapy depending on tumor type and location.',
                'weight': 0.95
            },
            'memory_loss': {
                'disease': 'Brain Tumor',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'EMERGENCY: See a neurologist immediately. MRI/CT scan required. Treatment may include surgery, radiation therapy, or chemotherapy depending on tumor type and location.',
                'weight': 0.85
            },
            'personality_changes': {
                'disease': 'Brain Tumor',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'EMERGENCY: See a neurologist immediately. MRI/CT scan required. Treatment may include surgery, radiation therapy, or chemotherapy depending on tumor type and location.',
                'weight': 0.85
            },
            'weakness': {
                'disease': 'Brain Tumor',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'EMERGENCY: See a neurologist immediately. MRI/CT scan required. Treatment may include surgery, radiation therapy, or chemotherapy depending on tumor type and location.',
                'weight': 0.8
            },
            'unexplained_weight_loss': {
                'disease': 'Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See an oncologist immediately. Full body scan required. Treatment may include chemotherapy, radiation therapy, immunotherapy, or surgery depending on cancer type and stage.',
                'weight': 0.95
            },
            'persistent_cough': {
                'disease': 'Lung Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a pulmonologist immediately. Chest X-ray and CT scan required. Treatment may include surgery, chemotherapy, radiation therapy, or targeted therapy.',
                'weight': 0.9
            },
            'blood_in_sputum': {
                'disease': 'Lung Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a pulmonologist immediately. Chest X-ray and CT scan required. Treatment may include surgery, chemotherapy, radiation therapy, or targeted therapy.',
                'weight': 0.95
            },
            'difficulty_swallowing': {
                'disease': 'Esophageal Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a gastroenterologist immediately. Endoscopy and biopsy required. Treatment may include surgery, chemotherapy, radiation therapy, or immunotherapy.',
                'weight': 0.9
            },
            'blood_in_stool': {
                'disease': 'Colon Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a gastroenterologist immediately. Colonoscopy and biopsy required. Treatment may include surgery, chemotherapy, radiation therapy, or immunotherapy.',
                'weight': 0.95
            },
            'change_in_bowel_habits': {
                'disease': 'Colon Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a gastroenterologist immediately. Colonoscopy and biopsy required. Treatment may include surgery, chemotherapy, radiation therapy, or immunotherapy.',
                'weight': 0.85
            },
            'breast_lump': {
                'disease': 'Breast Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a breast specialist immediately. Mammogram and biopsy required. Treatment may include surgery, chemotherapy, radiation therapy, or hormone therapy.',
                'weight': 0.95
            },
            'skin_changes': {
                'disease': 'Skin Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a dermatologist immediately. Skin biopsy required. Treatment may include surgery, radiation therapy, or immunotherapy.',
                'weight': 0.9
            },
            'abnormal_bleeding': {
                'disease': 'Cervical Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a gynecologist immediately. Pap smear and biopsy required. Treatment may include surgery, chemotherapy, radiation therapy, or immunotherapy.',
                'weight': 0.9
            },
            'abdominal_pain': {
                'disease': 'Liver Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a hepatologist immediately. CT scan and biopsy required. Treatment may include surgery, chemotherapy, radiation therapy, or targeted therapy.',
                'weight': 0.85
            },
            'jaundice': {
                'disease': 'Liver Cancer',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See a hepatologist immediately. CT scan and biopsy required. Treatment may include surgery, chemotherapy, radiation therapy, or targeted therapy.',
                'weight': 0.9
            },
            'swollen_lymph_nodes': {
                'disease': 'Lymphoma',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See an oncologist immediately. Lymph node biopsy required. Treatment may include chemotherapy, radiation therapy, immunotherapy, or stem cell transplant.',
                'weight': 0.85
            },
            'night_sweats': {
                'disease': 'Lymphoma',
                'severity': 'High',
                'urgency': 'Urgent',
                'cure': 'URGENT: See an oncologist immediately. Lymph node biopsy required. Treatment may include chemotherapy, radiation therapy, immunotherapy, or stem cell transplant.',
                'weight': 0.8
            },
    }

    # Lab test result indicators
    TEST_INDICATORS = {
        "fever": {"high": "Infection", "moderate": "Inflammation"},
        "cough": {"severe": "Respiratory Issue", "mild": "Irritation"},
        "shortness_of_breath": {"severe": "Lung/Cardiac Issue", "mild": "Anxiety"},
        "chest_pain": {"severe": "Cardiac Emergency", "mild": "Muscle Strain"},
        "fatigue": {"severe": "Chronic Condition", "mild": "Lifestyle"}
    }

    @staticmethod
    def predict(symptoms_list: List[str], age: int = None,
                gender: str = None, test_results: Dict = None) -> Dict:
        """
        Advanced prediction with multiple disease probabilities
        """
        selected = [s.lower().strip() for s in symptoms_list]
        predictions = []

        for disease, data in AdvancedAIHealthEngine.KNOWLEDGE_BASE.items():
            score = 0
            total_weight = 0

            # Calculate weighted match score
            for symptom, weight in data['symptoms'].items():
                if symptom in selected:
                    score += weight
                    total_weight += weight

            # Normalize score
            if total_weight > 0:
                final_score = score / total_weight
            else:
                final_score = 0

            # Adjust for age factor (elderly more susceptible)
            if age and age > 60:
                final_score *= 1.1
            elif age and age < 18:
                final_score *= 0.9

            # Adjust for test results if provided
            if test_results:
                for test, value in test_results.items():
                    if test in data['symptoms']:
                        final_score *= (1 + (value * 0.1))

            # Adjust for number of symptoms
            if len(selected) > 0:
                final_score = final_score * (1 + (len(selected) * 0.03))

            if final_score > 0.3:  # Minimum threshold
                predictions.append({
                    "disease": disease,
                    "probability": round(final_score * 100, 2),
                    "severity": data['severity'],
                    "urgency": data['urgency'],
                    "cure": data['cure'],
                    "test_recommended": data['test_recommended']
                })

        # Sort by probability
        predictions.sort(key=lambda x: x['probability'], reverse=True)

        # Get top 3 predictions
        top_predictions = predictions[:3]

        # Determine overall severity
        if top_predictions:
            max_severity = max([p['severity'] for p in top_predictions])
            severity_order = {"Low": 1, "Medium": 2, "High": 3, "Urgent": 4}
            overall_severity = max_severity
        else:
            overall_severity = "Unknown"

        return {
            "predictions": top_predictions,
            "overall_severity": overall_severity,
            "confidence": top_predictions[0]['probability'] if top_predictions else 0,
            "test_recommendations": [p for p in top_predictions if p['test_recommended']],
            "symptoms_analyzed": selected,
            "age_factor": age,
            "gender_factor": gender
        }

    @staticmethod
    def get_severity_color(severity: str) -> str:
        """Get color based on severity"""
        colors = {
            "Low": "success",
            "Medium": "warning",
            "High": "danger",
            "Urgent": "danger",
            "Unknown": "secondary"
        }
        return colors.get(severity, "secondary")