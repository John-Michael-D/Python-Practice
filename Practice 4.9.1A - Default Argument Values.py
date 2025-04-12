#It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.
#The most useful form is to specify a default value for one or more arguments.
#This creates a function that can be called with fewer arguments than it is defined to allow.
#For example:

def ask_ok(prompt, retries=4, reminder = "Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError("Invalid user response.")
        print(reminder)

#This function can be called in several ways:
#1 - Giving only the mandatory argument: ask_ok("Do you really want to quit?")
#2 - Giving one of the optional arguments: ask_ok("OK to overwrite file?", 2)
#3 - Or giving all arguments: ask_ok("OK to overwrite file?", 2, "Come on only yes or no!)
#This example also introduces the in keyword. This tests whether or not a sequence contains a certain value.

#The default values are evaluated at the point of function definition in the defining scope, so that:

i = 5

def f(arg=i):
    print(arg)

i = 6

f()

#Important warning: The default value is only evaluated once.
#This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
#For example, the following function accumulates the arguments passed to it on subsequent calls:

def g(a, L=[]):
    L.append(a)
    return L

print(g(1))
print(g(2))
print(g(3))

#If you don't want the default to be shared between subsequent calls, you can write the function like this instead:

def h(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(g(1))
print(g(2))
print(g(3))
