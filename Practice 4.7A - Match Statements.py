#A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
#Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.
#The simplest form compares a subject value against one or more literals:

def http_error(status):
    match status:
        case "400":
            return "Bad request"
        case "404":
            return "Not found"
        case "418":
            return "I'm a teapot"
        case "419" | "420" | "421":
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

while True:
    try:
        call = http_error(str(input(f"\nWhat kind of error is appearing on screen?")))
        print(call)
        question = str(input(f"\nWould you like to submit another error? (y/n)")).lower()
        if question == "y":
            continue
        elif question == "n":
            break
        else:
            print("Invalid entry! Only enter y or n.")
    except ValueError:
        continue

print("\nThanks for submitting your errors! Have a good one!")

