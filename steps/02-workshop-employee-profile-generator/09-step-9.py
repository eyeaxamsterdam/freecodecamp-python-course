"""
Step 9
Update the `employee_info` assignment to also concatenate `employee_age` at the end, using the `+` operator.

Once you've done so, you'll see a `TypeError` in the terminal. In the next step, you'll work on fixing it.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-9
"""

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
# --fcc-editable-region--
employee_info = full_name + ' is ' + employee_age
# --fcc-editable-region--
