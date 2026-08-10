"""
Step 11
Now complete the sentence by updating the employee_info assignment to also concatenate the string  years old at the end, using the + operator. Remember to include a space at the beginning of your string.

Finally, print employee_info.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-11
"""

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
# --fcc-editable-region--
employee_info = full_name + ' is ' + str(employee_age)

# --fcc-editable-region--
