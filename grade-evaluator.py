import csv
import os

def load_csv_data():
    filename = "grades.csv"
    if not os.path.exists(filename):
        return None
    assignments = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            assignments.append({
                'assignment': row['assignment'], 
                'group': row['group'], 
                'score': float(row['score']), 
                'weight': float(row['weight'])
            })
    return assignments

def evaluate_grades(data):
    f_score, s_score = 0, 0
    for item in data:
        contrib = (item['score'] / 100) * item['weight']
        if item['group'] == 'Formative': f_score += contrib
        else: s_score += contrib
    total = f_score + s_score
    gpa = (total / 100) * 5.0
    
    print("\n--- Evaluation Report ---")
    # Using .format() instead of f-strings for compatibility
    print("Final Grade: {0}%".format(round(total, 2)))
    print("GPA: {0} / 5.0".format(round(gpa, 2)))
    
    if f_score >= 30 and s_score >= 20:
        print("STATUS: PASSED")
    else:
        print("STATUS: FAILED")

if __name__ == "__main__":
    course_data = load_csv_data()
    if course_data:
        evaluate_grades(course_data)
    else:
        print("Error: grades.csv not found.")
