python


"""


Student Grade Calculator


 


Version: 1.0.0


"""


 


def calculate_average(marks):


    """Calculate
the average of a list of marks."""


    if not marks:


        return 0


    return sum(marks) / len(marks)


 


def get_result(average):


    """Determine whether the student
passed or failed."""


    if average >= 50:


        return "PASS"


    else:


        return "FAIL"


 


def main():


    student_name = input("Enter student name:
")


 


    marks = [


        float(input("Enter marks for subject
1: ")),


        float(input("Enter marks for subject
2: ")),


        float(input("Enter marks for subject
3: "))


    ]


 


    average = calculate_average(marks)


    result = get_result(average)


 


    print("\nStudent:", student_name)


    print("Average:", round(average, 2))


    print("Result:", result)


 


if __name__ == "__main__":


    main()
