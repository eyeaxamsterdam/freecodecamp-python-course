"""
Step 8
The bill is split, but division often results in long decimal numbers. Since money is typically represented with two decimal places, you should round the final result.

In an earlier lesson, you learned about the `round()` function which takes two arguments: the number you want to round and the number of decimal places to keep. Here's an example:

    num = 4.815162342
    round(num, 3) # 4.815

Use the `round()` function to round `final_bill` to two decimal places and assign the result to a new variable named `each_pays`.

Finally, use `print()` to display the string `Each person pays:` followed by a space and your `each_pays` variable.

With that, the bill splitter workshop is complete.

Link: https://www.freecodecamp.org/learn/python-v9/workshop-bill-splitter/step-8
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

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# --fcc-editable-region--
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')
# --fcc-editable-region--
