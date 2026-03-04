// diagnosis_app/static/js/main.js

// API Testing Functions
function testDiagnoseAPI() {
    fetch('/api/diagnose/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            symptoms: ["fever", "cough", "fatigue"],
            age: 30,
            gender: "Male"
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('apiResponse').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('apiResponse').textContent = 'Error: ' + error;
    });
}

function testHistoryAPI() {
    fetch('/api/history/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('apiResponse').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('apiResponse').textContent = 'Error: ' + error;
    });
}

function testPatientsAPI() {
    fetch('/api/patients/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('apiResponse').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById('apiResponse').textContent = 'Error: ' + error;
    });
}

// Search Functionality
document.getElementById('searchInput')?.addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();
    const rows = document.querySelectorAll('#historyTable tr');

    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(searchValue) ? '' : 'none';
    });
});

// Filter Functionality
document.getElementById('severityFilter')?.addEventListener('change', function() {
    const filterValue = this.value;
    const rows = document.querySelectorAll('#historyTable tr');

    rows.forEach(row => {
        const severity = row.querySelector('.badge')?.textContent;
        if (filterValue === '' || severity === filterValue) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});

// Form Validation
document.getElementById('diagnosisForm')?.addEventListener('submit', function(e) {
    const symptoms = document.querySelectorAll('.symptom-checkbox:checked');

    if (symptoms.length === 0) {
        e.preventDefault();
        alert('Please select at least one symptom!');
        return false;
    }

    const submitBtn = this.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Analyzing...';

    return true;
});

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('AI Healthcare Diagnosis System Loaded Successfully!');
});