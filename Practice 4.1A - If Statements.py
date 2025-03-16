#If statements are a useful way to have the script check for a condition or a series of conditions.
#If statements are usually used along with elif and else statements:

var_2 = []

while True:
    while True:
        try:
            var_1 = int(input("\nDear user, please input an integer: "))
            if var_1 % 2 == 0:
                var_2.append(var_1)
                print(f"\n{var_1} is an even number. Here are the numbers you've checked so far: {var_2}.")
                break
            else:
                var_2.append(var_1)
                print(f"\n{var_1} is an odd number. Here are the numbers you've checked so far: {var_2}.")
                break
        except KeyboardInterrupt:
            print("\nHave a good one, dear user!")
            break
        except ValueError:
            print("\nInvalid entry! Enter a valid integer value.")
            continue
    try:
        request = input("\nDear user, would you like to keep working? (Yes/No): ").strip().lower()
        if request not in ["yes", "no"]:
            print("\nInvalid entry! Please enter yes or no.")
            continue
        elif request == "yes":
            continue
        else:
            print("Have a good one, dear user!")
            break
    except KeyboardInterrupt:
        print("\nHave a good one, dear user!")