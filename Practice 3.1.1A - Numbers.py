print(f"2 + 2 equals {2+2}.")
print(f"\n50 - 5*6 equals {50 - 5*6}. Notice how Python uses the order of operations!")
print(f"\n(50 - 5*6) / 4 equals {(50 - 5*6) / 4}. You can also use parentheses to group operations!")
print(f"\n8 / 5 equals {8 / 5}. Notice how division in Python always returns a floating-point number, which is a number that includes a decimal.")

#Note that the "int" type lacks the decimal, which distinguishes it from the "float" type.

print(f"\n17 / 3 equals {17 / 3}. Notice how this normal kind of division will always result in a 'float' type.")
print(f"\nTo make the division operation result in an 'int' type and not a 'float' type, we must use floor division: 17 // 3 equals {17 // 3}.")
print(f"\nWe can also find the remainder in a division operation by using '%' operator: The remainder of 17 divided by 3 is {17 % 3}.")

print(f"\nWe can also calculate powers in Python by using the '**' operator: 5 squared equals {5 ** 2}.")

#Note that Python will also allow the user to assign 'int' or 'float' values to variables and the user can perform arithmetic operations on those variables.

width = 5
height = 2.75

print(f"\nWe have a rectangle with a width of {width} and a height of {height}. To find the area, we must multiply the width by the height.\nThe area of this rectangle is {width * height}.")

#Note that using both 'int' and 'float' types in a single arithmetic expression will result in Python converting the output to a 'float' type.

complex_numbers = 2 + 5j + 3j
print(f"\nPython can support arithmetic expressions involving complex numbers by indicating imaginary numbers with the 'j' suffix.\nFor example, 2 + 5j + 3j equals {complex_numbers}.")