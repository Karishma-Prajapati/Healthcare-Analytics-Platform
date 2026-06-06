def suggest_doctors(disease):

    doctors = {

        "Heart Disease": [

            "Dr. Raman Sharma (Cardiologist)",
            "Dr. Suraj Verma (Heart Specialist)",
            "Dr. Neha Kapoor (Cardiac Consultant)"

        ],

        "Diabetes": [

            "Dr. Vishal Gupta (Diabetologist)",
            "Dr. Karishma Mehta (Endocrinologist)",
            "Dr. Rohit Jain (Diabetes Specialist)"

        ]
    }

    return doctors.get(
        disease,
        ["Consult a specialist"]
    )