# Mapping of grades to grade points (IITM BS system)
GRADE_POINTS = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 4,
}

def calculate_cgpa(grades, credits):
    total_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        grade = grade.strip().upper()
        credit = float(credit)

        if grade not in GRADE_POINTS:
            raise ValueError(f"Invalid grade: {grade}")

        total_points += GRADE_POINTS[grade] * credit
        total_credits += credit

    if total_credits == 0:
        return 0.0  # Avoid division by zero, return 0 CGPA if no subjects selected

    return round(total_points / total_credits, 2)


def calculate_category_wise_cgpa(selected_subjects):
    """
    Calculate CGPA separately for Foundation, Diploma in Programming, and Diploma in Data Science.
    selected_subjects: List of tuples containing (subject_name, category, grade, credits)
    """
    category_wise_data = {
        "Foundation": {"grades": [], "credits": []},
        "Diploma in Prog": {"grades": [], "credits": []},
        "Diploma in Data": {"grades": [], "credits": []},
    }

    for subject_name, category, grade, credit in selected_subjects:
        print(category)
        if category in category_wise_data:
            category_wise_data[category]["grades"].append(grade)
            category_wise_data[category]["credits"].append(credit)

    foundation_cgpa = calculate_cgpa(category_wise_data["Foundation"]["grades"], category_wise_data["Foundation"]["credits"])
    diploma_prog_cgpa = calculate_cgpa(category_wise_data["Diploma in Prog"]["grades"], category_wise_data["Diploma in Prog"]["credits"])
    diploma_data_cgpa = calculate_cgpa(category_wise_data["Diploma in Data"]["grades"], category_wise_data["Diploma in Data"]["credits"])

    # Calculate overall CGPA (considering all subjects)
    all_grades = category_wise_data["Foundation"]["grades"] + category_wise_data["Diploma in Prog"]["grades"] + category_wise_data["Diploma in Data"]["grades"]
    all_credits = category_wise_data["Foundation"]["credits"] + category_wise_data["Diploma in Prog"]["credits"] + category_wise_data["Diploma in Data"]["credits"]
    total_cgpa = calculate_cgpa(all_grades, all_credits)

    return foundation_cgpa, diploma_prog_cgpa, diploma_data_cgpa, total_cgpa
