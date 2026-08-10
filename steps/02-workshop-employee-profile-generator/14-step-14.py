"""
Step 14
Currently, employee_card only shows the employee's name. Now you're going to add more information to it. 

Update the employee_card assignment to include the employee's age. The final string should look like this: Employee: [name] | Age: [age] with [name] replaced with the employee's name, and [age] replaced with the employee's age.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-14
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
# --fcc-editable-region--
employee_card = f'Employee: {full_name}'
# --fcc-editable-region--
