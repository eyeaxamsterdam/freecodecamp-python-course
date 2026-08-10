"""
Step 17
You can slice from any part of the string, not just the beginning. And it is helpful in many cases.

Create a variable year_code and assign it the slice of employee_code from index 4 to 8. This will extract 2026.

Then create a variable initials and assign it the slice of employee_code from index 9 to 11. This will extract JD.

Finally, print both variables to the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-17
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
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department) 
# --fcc-editable-region--

# --fcc-editable-region--
