#By default, arguments may be passed to a Python function either by position or explicitly by keyword.
#For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine:
#If the items are passed by position, by position or keyword, or by keyword.
#If / or * are not present in the function definition arguments may be passed to a function by position or keyword.
#Positional-only parameters are placed before a /
#The / is used to logically separate the positional-only parameters from the rest of the parameters.
#If there is no / in the function definition, there are no positional-only parameters.
#Parameters following the / may be positional-or-keyword or keyword-only.
#To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameters.
#Consider the following example function definitions paying close attention to the markers / and *:
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

#The first function definition, standard_arg, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:
standard_arg(2)
standard_arg(arg=2)

#The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function definition:
pos_only_arg(1)
#pos_only_arg(arg=1) will generate an error.

#The third function kwd_only_arg only allows keyword arguments as indicated by a * in the function definition:
kwd_only_arg(arg=3)
#kwd_only_arg(3) will generate an error.

#And the last uses all three calling conventions in the same function definition:
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
#combined_example(1, 2, 3) will generate an error.
#combined_example(pos_only=1, standard=2, kwd_only=3) will generate an error.

#As guidance:
#1. Use positional-only if you want the name of the parameters to not be available to the user.
#This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.
#2. Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.
#3. For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.












