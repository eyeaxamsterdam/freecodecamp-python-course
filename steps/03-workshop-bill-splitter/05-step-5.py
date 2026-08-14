"""
Step 5
The service was excellent, so the group decides to leave a 25% tip. To calculate a percentage in Python, you can multiply the total by the decimal equivalent of the percentage.

For example, to find 10% of a value, you would multiply it by `0.10` using the `*` operator:

    tax = total * 0.10

Create a variable named `tip` and assign it the result of multiplying `running_total` by `0.25`.

Finally, use `print()` to display the string `Tip amount:` followed by a space and the value of your `tip` variable.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-bill-splitter/step-5
"""

running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# --fcc-editable-region--
tip = running_total * 0.25
print(f'Tip amount: {tip}')
# --fcc-editable-region--
