#Functions can also be called using keyword arguments of the form kwarg = value.
#For instance, the following function accepts one required argument (voltage) and three optional arguments (state, action, and type):

def parrot(voltage, state="a stiff", action = "voom", type = "Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#This function can be called in any of the following ways:

parrot(1000) #1 positional argument
parrot(voltage=1000) #1 keyword argument
parrot(voltage=1000000, action='VOOOOOM') #2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000) #2 keyword arguments
parrot('a million', 'bereft of life', 'jump') #3 positional arguments
parrot('a thousand', state='pushing up the daisies') #1 positional, 1 keyword

#But all the following calls would be invalid:

#parrot() Required argument missing
#parrot(voltage=5.0, 'dead')  Non-keyword argument after a keyword argument
#parrot(110, voltage=220) Duplicate value for the same argument
#parrot(actor="John Cleese") #Unknown keyword argument

#In a function call, keyword arguments must follow positional arguments.
#All the keyword arguments passed must match one of the arguments accepted by the function, and their order is not important.
#This also includes non-optional arguments.
#No argument may receive a value more than once.
#Here's an example that fails due to this restriction:

def function(a):
    pass

#function(0, a=0)

#When a final parameter of the form **name is passed, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter.
#This may be combined with a formal parameter of the form *name which receives a tuple containing the positional arguments beyond the formal parameter list.
#*name must occur before **name
#For example:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

print(f"\n")

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

