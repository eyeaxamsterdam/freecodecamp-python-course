"""
Step 9
The output is False, which shows that score is not an int.

Another common kind of number in Python is float, which represents a number with decimals. Replace int with float in the existing isinstance() call to confirm this.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-report-card-printer/step-9
"""

name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
# --fcc-editable-region--
print(isinstance(score, int))
# --fcc-editable-region--
