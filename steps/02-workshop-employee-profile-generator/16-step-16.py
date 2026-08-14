"""
Step 16
When working with strings, you'll often need to extract a specific portion of a string. This is called **slicing**.

The syntax is `string[start:stop]`, where:

* `start` is the index where the slice begins (**inclusive**).
* `stop` is the index where the slice ends (**exclusive**).

For example, if `text = 'Python'`, then `text[0:2]` gives `'Py'`.

Define `employee_code` as `'DEV-2026-JD-001'`. After that, create a variable `department` and assign it the slice of `employee_code` from index `0` to `3`. Then print `department` to the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-16
"""

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# --fcc-editable-region--
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
# --fcc-editable-region--
