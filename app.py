# WITH CHECKBOXES

# from flask import Flask, render_template, request, redirect, url_for, flash, session
# from models import calculate_cgpa, GRADE_POINTS, calculate_category_wise_cgpa

# app = Flask(__name__)
# app.secret_key = "hello"

# # List of subjects and their respective credits
# SUBJECTS = [
#     {"name": "Computational Thinking", "credits": 4, "category": "Foundation"},
#     {"name": "English I", "credits": 4, "category": "Foundation"},
#     {"name": "Mathematics for Data Science I", "credits": 4, "category": "Foundation"},
#     {"name": "Statistics for Data Science I", "credits": 4, "category": "Foundation"},
#     {"name": "Programming in Python", "credits": 4, "category": "Foundation"},
#     {"name": "English II", "credits": 4, "category": "Foundation"},
#     {"name": "Mathematics for Data Science II", "credits": 4, "category": "Foundation"},
#     {"name": "Statistics for Data Science II", "credits": 4, "category": "Foundation"},
#     {"name": "Database Management Systems", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - I", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - II", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "System Commands", "credits": 3, "category": "Diploma in Prog"},
#     {"name": "Programming Concepts using Java", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Programming, Data Structures and Algorithms using Python", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - I [PROJECT]", "credits": 2, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - II [PROJECT]", "credits": 2, "category": "Diploma in Prog"},
#     {"name": "Machine Learning Foundations", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Business Data Management", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Machine Learning Techniques", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Machine Learning Practice", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Business Analytics", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Tools in Data Science", "credits": 3, "category": "Diploma in Data"},
#     {"name": "Business Data Management [PROJECT]", "credits": 2, "category": "Diploma in Data"},
#     {"name": "Machine Learning Practice [PROJECT]", "credits": 2, "category": "Diploma in Data"},
# ]

# @app.route("/")
# def home():
#     return render_template("index.html", subjects=SUBJECTS)

# def calculate_cgpa(grades, credits):
#     total_points = sum(GRADE_POINTS[grade] * credit for grade, credit in zip(grades, credits))
#     total_credits = sum(credits)
#     return round(total_points / total_credits, 2) if total_credits > 0 else 0

# @app.route("/")
# def index():
#     return render_template(
#         "index.html",
#         subjects=SUBJECTS,
#         foundation_cgpa=None,
#         diploma_prog_cgpa=None,
#         diploma_data_cgpa=None,
#         result=None
#     )


# @app.route("/calculate", methods=["POST"])
# def calculate():
#     selected_subjects = []
    
#     subjects_selected = request.form.getlist("subjects[]")  # Get selected subjects as a list

#     if not subjects_selected:
#         flash("No subjects selected! Please select at least one.", "error")
#         return redirect("/")

#     for subject in SUBJECTS:
#         subject_name = subject["name"]
#         category = subject["category"]
#         credits = subject["credits"]

#         if subject_name in subjects_selected:
#             grade = request.form.get(f"grade_{subject_name}")  # Fetch the corresponding grade
#             if not grade:
#                 flash("Please select grades for all selected subjects.", "error")
#                 return redirect("/")

#             selected_subjects.append((subject_name, category, grade, credits))

#     # Calculate CGPAs
#     print(selected_subjects)
#     foundation_cgpa, diploma_prog_cgpa, diploma_data_cgpa,result = calculate_category_wise_cgpa(selected_subjects)
#     print(diploma_data_cgpa)
#     # total_cgpa = calculate_cgpa(selected_subjects,credits=credits)

#     return render_template(
#         "index.html", 
#         subjects=SUBJECTS,
#         foundation_cgpa=foundation_cgpa,
#         diploma_prog_cgpa=diploma_prog_cgpa,
#         diploma_data_cgpa=diploma_data_cgpa,
#         result=result
#     )


# if __name__ == "__main__":
#     app.run(debug=True)




# NO CHECKBOXES

# from flask import Flask, render_template, request, redirect, flash
# from models import calculate_cgpa, GRADE_POINTS, calculate_category_wise_cgpa

# app = Flask(__name__)
# app.secret_key = "hello"

# # List of subjects and their respective credits
# SUBJECTS = [
#     {"name": "Computational Thinking", "credits": 4, "category": "Foundation"},
#     {"name": "English I", "credits": 4, "category": "Foundation"},
#     {"name": "Mathematics for Data Science I", "credits": 4, "category": "Foundation"},
#     {"name": "Statistics for Data Science I", "credits": 4, "category": "Foundation"},
#     {"name": "Programming in Python", "credits": 4, "category": "Foundation"},
#     {"name": "English II", "credits": 4, "category": "Foundation"},
#     {"name": "Mathematics for Data Science II", "credits": 4, "category": "Foundation"},
#     {"name": "Statistics for Data Science II", "credits": 4, "category": "Foundation"},
#     {"name": "Database Management Systems", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - I", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - II", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "System Commands", "credits": 3, "category": "Diploma in Prog"},
#     {"name": "Programming Concepts using Java", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Programming, Data Structures and Algorithms using Python", "credits": 4, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - I [PROJECT]", "credits": 2, "category": "Diploma in Prog"},
#     {"name": "Mordern Application Development - II [PROJECT]", "credits": 2, "category": "Diploma in Prog"},
#     {"name": "Machine Learning Foundations", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Business Data Management", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Machine Learning Techniques", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Machine Learning Practice", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Business Analytics", "credits": 4, "category": "Diploma in Data"},
#     {"name": "Tools in Data Science", "credits": 3, "category": "Diploma in Data"},
#     {"name": "Business Data Management [PROJECT]", "credits": 2, "category": "Diploma in Data"},
#     {"name": "Machine Learning Practice [PROJECT]", "credits": 2, "category": "Diploma in Data"},
# ]

# @app.route("/")
# def index():
#     return render_template("index.html", subjects=SUBJECTS, foundation_cgpa=None, diploma_prog_cgpa=None, diploma_data_cgpa=None, result=None)

# @app.route("/calculate", methods=["POST"])
# def calculate():
#     selected_subjects = []

#     for subject in SUBJECTS:
#         subject_name = subject["name"]
#         category = subject["category"]
#         credits = subject["credits"]

#         grade = request.form.get(f"grade_{subject_name}")  # Fetch grade directly
#         if grade:
#             selected_subjects.append((subject_name, category, grade, credits))

#     if not selected_subjects:
#         flash("Please select grades for at least one subject.", "error")
#         return redirect("/")

#     # Calculate CGPAs
#     foundation_cgpa, diploma_prog_cgpa, diploma_data_cgpa, result = calculate_category_wise_cgpa(selected_subjects)

#     return render_template(
#         "index.html", 
#         subjects=SUBJECTS,
#         foundation_cgpa=foundation_cgpa,
#         diploma_prog_cgpa=diploma_prog_cgpa,
#         diploma_data_cgpa=diploma_data_cgpa,
#         result=result
#     )

# if __name__ == "__main__":
#     app.run(debug=True)


# EXCEL UPLOAD

import pandas as pd
import os
from flask import Flask, render_template, request, redirect, flash

from models import calculate_category_wise_cgpa

app = Flask(__name__)
app.secret_key = "hello"

# Function to load subjects from Excel
def load_subjects():
    file_path = "subjects.csv"  # Default file

    # Check if CSV file exists, prioritize CSV over Excel
    if os.path.exists("subjects.csv"):
        file_path = "subjects.csv"

    # Read file based on its extension
    if file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    subjects = df.to_dict(orient="records")
    return subjects


# Load subjects at app start
SUBJECTS = load_subjects()

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def index():
    subjects = load_subjects()  # Load latest data from Excel
    return render_template("index.html", subjects=subjects, foundation_cgpa=None, diploma_prog_cgpa=None, diploma_data_cgpa=None, result=None)


@app.route("/calculate", methods=["POST"])
def calculate():
    subjects = load_subjects()  # Load latest data from Excel
    selected_subjects = []

    for subject in subjects:
        subject_name = subject["name"]
        category = subject["category"]
        credits = subject["credits"]

        grade = request.form.get(f"grade_{subject_name}")
        if grade:
            selected_subjects.append((subject_name, category, grade, credits))

    if not selected_subjects:
        flash("Please select grades for at least one subject.", "error")
        return redirect("/")

    foundation_cgpa, diploma_prog_cgpa, diploma_data_cgpa, result = calculate_category_wise_cgpa(selected_subjects)

    return render_template(
        "index.html", 
        subjects=subjects,
        foundation_cgpa=foundation_cgpa,
        diploma_prog_cgpa=diploma_prog_cgpa,
        diploma_data_cgpa=diploma_data_cgpa,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
