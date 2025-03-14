print("Normal text in Python comprises the 'str' type, which is also known as strings.")
print("\nSurrounding anything in double quotation marks will result in a str type.")
print('\nYou can also use single quotation marks, if you prefer.')

#When using quotation marks within a string, you need to use an escape \
print("\n\"Friends, Romans, Countrymen... Lend me your ears!\"")

#Alternatively, you can use single quotation marks within a string surrounded by double quotation marks or double quotation marks within a string surrounded by single quotation marks.
print("\n'Gallia est omnis divisa en partes tres.'")

#Note that in order to prevent special characters such as \ or \n to be interpreted, you must include an r before the statement.
print('\n'r"For example, the file directory C:\employees\names")

#String literals can span multiple lines. You can do this by using triple quotation marks. End of line characters are automatically included in string-literals but can be omitted by entering a \ at the end of the line.
print("""
User Menu: [OPTIONS]
        -d Derive
        -i Integrate
        -t Trigonometry
        -s Statistics\
""")

#Strings can be concatenated (added together) with the + operator and they can be repeated with the * operator.
print("\n" + "Romeo..." * 3 + " Where are fore art thou, Romeo?")

#Two or more string literals next to each other are automatically concatenated.
print("\nUnited " "States " "of " "America ")

#Variables and strings can be concatenated using the + operator.
var_1 = "Apples"
var_2 = ", Oranges"

print(f"\n{var_1}" + f"{var_2}" + ", and Pears.")

#Strings can be indexed, with the first character from the left having a value of 0 and the first character from the right having a value of -1.
var_3 = "South Carolina"

print("\n", var_3[0], var_3[1], var_3[2], var_3[3], var_3[4])
print("\n", var_3[-8], var_3[-7], var_3[-6], var_3[-5], var_3[-4], var_3[-3], var_3[-2], var_3[-1])

#Strings can also be sliced, which will return a substring. Note that the value of the first index is included, but the value of the second index isn't included unless if it's the last character in the string.
print("\n", var_3[0:6], var_3[6:14])

#Note that an omitted first index will default to zero and an omitted second index will default to the size of the string.
print("\n", var_3[:])

#Slices can also be concatenated and repeated.
print("\n", var_3[0:6] + var_3[6:14])
print("\n", var_3[0:6] * 3)

#Note that strings are immutable. Once a string is assigned to a variable, the string itself cannot be changed.
#For example: print(var_3[1] = "L") will result in an error.
#If a different string is needed, simply create a different one.
print("\n", var_3 + " is a nice place to live.")

#The len() function will return the length of a string.
print("\n", len(var_3))