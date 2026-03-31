import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file (e.g., grades.csv): ")
    if not os.path.exists(filename):
        print("Error: File not found.")
        sys.exit(1)
    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    "assignment": row["assignment"].strip(),
                    "group": row["group"].strip(),
                    "score": float(row["score"]),
                    "weight": float(row["weight"])
                })
        return assignments
    except Exception as e:
        print("Error: {0}".format(e))
        sys.exit(1)

def evaluate_grades(data):
    print("\n--- Processing Grades ---")
    
    # Validation
    invalid = [i["assignment"] for i in data if not (0 <= i["score"] <= 100)]
    if invalid:
        print("Warning: Bad scores in assignments.")
    else:
        print("All scores are valid (0-100).")

    formative = [i for i in data if i["group"].lower() == "formative"]
    summative = [i for i in data if i["group"].lower() == "summative"]
    
    f_w = sum(i["weight"] for i in formative)
    s_w = sum(i["weight"] for i in summative)
    
    # Calculations
    f_p = sum((i["score"]/100)*i["weight"] for i in formative)/60*100 if f_w > 0 else 0
    s_p = sum((i["score"]/100)*i["weight"] for i in summative)/40*100 if s_w > 0 else 0
    final = sum((i["score"]/100)*i["weight"] for i in data)
    gpa = (final/100)*5.0

    print("\n=============================================")
    print("            FINAL EVALUATION REPORT")
    print("=============================================")
    print("  Formative  : {0:.2f}%".format(f_p))
    print("  Summative  : {0:.2f}%".format(s_p))
    print("  Final Grade: {0:.2f}%".format(final))
    print("  GPA        : {0:.2f} / 5.0".format(gpa))
    print("---------------------------------------------")
    print("  STATUS: {0}".format('PASSED' if (f_p >= 50 and s_p >= 50) else 'FAILED'))
    print("=============================================")

if __name__ == "__main__":
    course_data = load_csv_data()
    if course_data:
        evaluate_grades(course_data)
