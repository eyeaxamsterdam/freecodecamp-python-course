"""
Step 15
Now it's time to add the final details to the card.

Create a variable named `position` with the value of the string `Data Analyst` and a variable named `salary` with the value of the integer `75000`.

Then, update your `employee_card` f-string to include the position and salary. It should follow this exact format: `Employee: [full_name] | Age: [employee_age] | Position: [position] | Salary: $[salary]`. Replace the placeholders with the corresponding variables.

Finally, print `employee_card` to see the result.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-15
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

employee_card = f'Employee: {full_name} | Age: {employee_age}'
# --fcc-editable-region--
