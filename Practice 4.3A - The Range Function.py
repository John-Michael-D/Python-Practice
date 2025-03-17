#If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.
#It generates arithmetic progressions:
for i in range(5):
    print(i)

#Note that the ending point of a range is inclusive, but it is possible to change the starting point or the increment of the range.
print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))

#To iterate over the indices of a sequence, you can combine range() and len():
song = ["Mary", "had", "a", "little", "lamb"]
for index in range(len(song)):
    print(index, song[index])

#However, in such cases it's more convenient to use the enumerate() function:
print(list(enumerate(song)))

#A strange thing happens if you just print a range:
print(range(10))

#In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
#It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
#We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.
#We have seen that the for statement is such a construct, while an example of a function that takes an iterable is sum():
print(sum(range(4)))