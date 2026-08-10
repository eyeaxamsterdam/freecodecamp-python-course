"""
Step 12
Now you're going to use the str() function one more time. Just like with age, you must convert any numeric variable to a string before concatenating it with other text.

Create a variable named experience_years and assign it the integer 5.

Then, create a variable experience_info. Assign it a string formed by concatenating 'Experience: ', the experience_years variable (converted to a string), and ' years', using the + operator. Print the result to the terminal.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-12
"""

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
# --fcc-editable-region--

# --fcc-editable-region--
