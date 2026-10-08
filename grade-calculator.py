"""
Student Grade Calculator

Version: 1.1.0
"""

def calculate_average(marks):
    """Calculate the average of the marks."""
    return sum(marks) / len(marks)


def determine_grade(average):
    """Determine the grade based on the average."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    print("Student Grade Calculator")
    print("------------------------")

    student_name = input("Enter student name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    average = calculate_average(marks)
    grade = determine_grade(average)

    print("\nStudent Name:", student_name)
    print("Marks:", marks)
    print("Average:", average)
    print("Grade:", grade)

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")


if __name__ == "__main__":
    main()