"""
Step 10
As you can see Python raised a TypeError: can only concatenate str (not "int") to str. This happens because Python does not allow you to concatenate text (strings) and numbers (integers) directly.

To fix this, you must convert the number to a string first using the str() function, which returns the string version of an object:

    my_num = str(42)
    print(type(my_num)) # <class 'str'>

Update your employee_info assignment to convert employee_age to a string using str(employee_age).

Link: https://www.freecodecamp.org/learn/python-v9/workshop-employee-profile-generator/step-10
"""


