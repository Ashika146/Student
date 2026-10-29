
from student import calculate_total, calculate_average, get_result


def test_calculate_total():
    assert calculate_total([80, 90, 70]) == 240


def test_calculate_average():
    assert calculate_average([80, 90, 70]) == 80


def test_student_pass():
    assert get_result([80, 90, 70]) == "Pass"


def test_student_fail():
    assert get_result([80, 30, 70]) == "Fail"


def test_invalid_marks():
    assert get_result([80, 110, 70]) == "Invalid marks"


def test_empty_marks():
    assert calculate_average([]) == 0
