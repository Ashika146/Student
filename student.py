
def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def get_result(marks):
    if not marks:
        return "No marks provided"

    if any(mark < 0 or mark > 100 for mark in marks):
        return "Invalid marks"

    if any(mark < 35 for mark in marks):
        return "Fail"

    return "Pass"


if __name__ == "__main__":
    student_name = "Ashika"
    marks = [85, 90, 78, 88, 92]

    print("Student Marks Calculator")
    print("------------------------")
    print("Student:", student_name)
    print("Marks:", marks)
    print("Total:", calculate_total(marks))
    print("Average:", round(calculate_average(marks), 2))
    print("Result:", get_result(marks))
