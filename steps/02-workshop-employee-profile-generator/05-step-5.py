"""
Step 5
Now, your address seems incomplete. You also want to add the apartment number where the employee lives, so you should modify the variable.  

When you want to add content to the end of an existing string variable, you can use the **augmented assignment** operator, `+=`. This is shorter than writing `var = var + 'new text'`. For example:  

    greeting = 'Hello'
    greeting += ' World'
    print(greeting) # Hello World

Remember that strings are immutable, therefore this operation does not change the original string. Instead it creates a new string and reassigns it to the variable.

Use the `+=` operator to add the string `, Apartment 4B` to your `address` variable.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-5
"""

first_name = 'John'
last_name = 'Doe'
print(first_name)
print(last_name)
full_name = first_name + ' ' + last_name
print(full_name)
address = '123 Main Street'  
address += ', Apartment 4B'
# --fcc-editable-region--
employee_age = 28
# --fcc-editable-region--
