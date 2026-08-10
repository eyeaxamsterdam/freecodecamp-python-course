"""
Step 13
Concatenating many strings using `+` and converting numbers using `str()` can get messy and hard to read.

Python 3.6 introduced **f-strings** to solve this. By adding the letter `f` before the opening quote, you can put variables and expressions inside replacement fields represented by curly braces `{}`. For example:

    name = 'John'
    print(f'Hello {name}') # Output: Hello John

Create a variable `employee_card` and assign it an f-string that displays `Employee:` followed by a space and the value of the `full_name` variable.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-13
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

# --fcc-editable-region--
