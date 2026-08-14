"""
Step 8
Now, add the student's score.

Declare a variable named `score` and assign it the value `80.5`.

Although both `age` and `score` are numbers, they may not be the same kind. Python provides a function called `isinstance()` to check this.

    x = 10
    print(isinstance(x, int)) # Output: True

Use `isinstance()` to check whether `score` is an `int`, and print the result to the terminal as shown in the example above.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-report-card-printer/step-8
"""

name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

# --fcc-editable-region--
score = 80.5
print(isinstance(score, int))
# --fcc-editable-region--