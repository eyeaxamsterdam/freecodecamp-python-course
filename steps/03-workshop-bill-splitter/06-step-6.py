"""
Step 6
Now that you have calculated the tip, you need to add it to your `running_total` to find the final bill amount.

Use the `+=` operator to add the value of `tip` to your `running_total`. Finally, use `print()` to display the string `Total with tip:` followed by a space and the value of `running_total`.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-bill-splitter/step-6
"""

running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

# --fcc-editable-region--
running_total += tip
print(f'Total with tip: {running_total}')
# --fcc-editable-region--
