#The pass statement does nothing.
#It can be used when a statement is required syntactically but the program requires no action.
#For example:

while True:
    pass #Busy-wait for keyboard interrupt (Ctrl+C)

#This is commonly used to creating minimal classes:

class MyEmptyClass:
    pass

#Another place pass can be used is as a place-holder for a function or conditional body.
#This is useful when you are working on new code and want to think abstractly:

def initlog(*args):
    pass #Remember to implement this!
