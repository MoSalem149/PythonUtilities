def grade_category(average_grade):
    if average_grade >= 85:
        return "Excellent"
    elif average_grade >= 75:
        return "Very Good"
    elif average_grade >= 65:
        return "Good"
    elif average_grade >= 50:
        return "Pass"
    else:
        return "Fail"

num_subjects = int(input("Enter the number of subjects: "))
subjects = []
grades = {}

for i in range(num_subjects):
    subject = input(f"Enter the name of subject {i + 1}: ")
    grade = float(input(f"Enter the grade for {subject}: "))
    subjects.append(subject)
    grades[subject] = grade

max_grade = max(grades.values())
min_grade = min(grades.values())
average_grade = sum(grades.values()) / num_subjects
category = grade_category(average_grade)

print("\nGrade Summary:")
print("---------------")
print(f"Maximum Grade: {max_grade}")
print(f"Minimum Grade: {min_grade}")
print(f"Average Grade: {average_grade}")
print(f"Overall Grade Category: {category}")

print("\nSubjects and Grades (Sorted by Grade):")
print("---------------")
sorted_grades = sorted(grades.items(), key=lambda x: x[1], reverse=True)
for subject, grade in sorted_grades:
    print(f"{subject}: {grade}")
