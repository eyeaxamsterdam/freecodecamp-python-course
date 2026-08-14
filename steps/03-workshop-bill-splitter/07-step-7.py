"""
Step 7
With the tip now included, you have the final amount for the entire group. You have to determine how much each person owes by dividing the total bill by the number of friends. 

In Python, you use the forward slash `/` to perform division. For example:

    half = 10 / 2

Create a variable named `final_bill` and assign it the result of dividing `running_total` by `num_of_friends`. 

Finally, use the `print()` function to display the string `Bill per person:` followed by a space and the value of `final_bill`.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-bill-splitter/step-7
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

running_total += tip
print('Total with tip:', running_total)

# --fcc-editable-region--
final_bill = running_total / num_of_friends
print(f'Bill per person: {final_bill}')
# --fcc-editable-region--
