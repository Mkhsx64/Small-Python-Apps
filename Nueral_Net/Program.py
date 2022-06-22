import numpy as np

#checking out numpy functions
#grading check

CURVE_CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])
def curve(grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return print(np.clip(new_grades, grades, 100))

curve(grades)
