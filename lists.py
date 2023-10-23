#List comprehensions simply make your code more compact when performing tasks concerning lists.
# Let's look at a couple of examples.

"""Say you have a list: years = [1998, 1987, 2001, 1993, 2010, 1967, 1999]"""
"""Now you want to get a list of ages from those years. A normal way to go about this would be:"""

#1. Create an empty list called "ages."

years = [1998, 1987, 2001, 1993, 2010, 1967, 1999]
ages = []

#2. Use a for loop that calculates the age of each year in the "years" list and appends it to the "ages" list.
for year in years:
    a = (2023 - year)
    ages.append(a)
print(ages) 

"""That works just fine, but list comprehesion would accomplish the same task in a more compact manner."""

#Look at the list comprehension solution below:

years = [1998, 1987, 2001, 1993, 2010, 1967, 1999]
ages_2 = [2023 - year for year in years]
print(ages_2)

#Both solutions will give the same result.
