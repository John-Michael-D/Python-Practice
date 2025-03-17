#The break statement breaks out of the innermost enclosing for or while loop:
for n in range(2,10):
    for x in range (2,n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

#The continue statement continues with the next iteration of the loop:
for num in range(2,10):
    if num % 2 == 0:
        print(f"Found an even number: {num}.")
        continue
    print(f"Found an odd number: {num}.")
