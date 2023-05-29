# %% 4
def majority_element(_list):
    counter = 0
    num = _list[0]
    for i in _list:
        frequency = _list.count(i)
        if (frequency > counter):
            counter = frequency
            num = i
    return num


def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3
    result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result1 == 2


test_majority_element()
# %% 5


def get_subjects_not_passed_by_all_students(student_exams):
    not_passed_subjects = set()
    for exam in student_exams:
        name_, score, subject = exam
        if score < 60:
            not_passed_subjects.add(subject)
    return not_passed_subjects


def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 85, "Math"),
        ("Bob", 59, "Math"),
        ("Charlie", 65, "Math"),
        ("Alice", 90, "Science"),
        ("Bob", 80, "Science"),
        ("Charlie", 32, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]
    assert get_subjects_not_passed_by_all_students(exams) == {
        "Science", "Math"}


test_get_subjects_not_passed_by_all_students()
# %%
