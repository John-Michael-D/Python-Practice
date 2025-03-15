#Lists are compound data types in Python that contain items separated by commas and surrounded by brackets.
var_1 = [1, 2, 3, 4, 5, 6, 7, 8]
var_2 = ["Alpha", "Bravo", "Charlie", 9, 10]
print(f"This is an example of a string: {var_1}.")
print(f"\nStrings can contain different data types: {var_2}.")

#Lists can be indexed and sliced much like strings.
print(f"\nFor example, this is the third value in the var_1 list: {var_1[2]}.")
print(f"\nAnd this is the second value in the var_2 list: {var_2[1]}.")
print(f"\nLastly, this is a slice of the last 3 items in the var_2 list: {var_2[-3:]}.")

#Lists can also be concatenated.
print("\n", var_1 + var_2)

#Lists are a mutable type, and their contents can be changed.
print(f"\nHere's the original var_2 list: {var_2}.")
var_2[0] = "Apple"
print(f"\nAnd here's the var_2 list with the first item being replaced with another value: {var_2}.")

#New items can be attached to the end of a list by using .append()
var_2.append(11)
print(f"\nHere's the var_2 list with a new item at the end: {var_2}.")

#The len() function can be used to count the number of items within a list.
print(f"\nHere are the number of items in the var_2 list: {len(var_2)}.")

#Lists can also be nested and be indexed.
var_3 = [var_1, var_2]
print(f"\nHere's a list containing both the var_1 and var_2 lists: {var_3}.")
print(f"\nHere's the result for var_3[0][0]: {var_3[0][0]}. Here's the result for var_3[1][0]: {var_3[1][0]}.")