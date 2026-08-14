"""
Step 4
Now that you have stored the individual costs, you can calculate the total. 

Recall that the `+=` operator adds a value to an existing variable and updates it at the same time. For example:

    total = 10
    total += 2 + 2 + 1
    print(total)  # total is now 15

Use the `+=` operator once to add `appetizers`, `main_courses`, `desserts`, and `drinks` to `running_total`.

Finally, use `print()` to display the string `Total bill so far:` followed by a space and the value of `running_total`.

**Note:** You might notice that the output has more decimal digits than expected. As you learned in a previous lesson, this happens because numbers are stored in binary, and many decimal values cannot be represented exactly in this format, which leads to rounding errors.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-bill-splitter/step-4
"""

running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# --fcc-editable-region--
running_total += appetizers + main_courses + desserts + drinks
print(f'Total bill so far: {running_total}')
# --fcc-editable-region--
