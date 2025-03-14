import random #Required for the script to pick values from two random iterations to perform the four arithmetic operations.

#Fibonacci Sequence:
#The sum of two elements defines the next.

a, b = 0, 1 #Establishes the initial values of the sequence.
iteration_count = 0 #Initializes the increment counter.
iteration_store = [] #Stores the iteration counts within a list for manipulation.

while a < 50:
    iteration_store.append(a) #Appends the current value of "a" to the iteration_store list.
    print(a, f"(Fibonacci Sequence Iteration = {iteration_count}.)")
    a, b = b, a+b
    iteration_count += 1 #Increases the counter by 1 with each iteration of the while loop.

#Randomly picks two iterations from iteration_store
random_iteration_1 = random.randint(0, len(iteration_store) - 1)
random_iteration_2 = random.randint(0, len(iteration_store) - 1)

#Aquires the corresponding values from the two randomly chosen iterations.
value_1 = iteration_store[random_iteration_1]
value_2 = iteration_store[random_iteration_2]

#Performs the four arithmetic operations on the chosen values.
addition = value_1 + value_2
subtraction = value_1 - value_2
multiplication = value_1 * value_2
division = value_1 / value_2 if value_2 != 0 else "Division by zero error."

#Prints the results
print("\nRandomly selected iterations and their values:")
print(f"Iteration {random_iteration_1}: {value_1}")
print(f"Iteration {random_iteration_2}: {value_2}")

print("\nArithmetic operations:")
print(f"Addition: {value_1} + {value_2} = {addition}")
print(f"Subtraction: {value_1} + {value_2} = {subtraction}")
print(f"Multiplication: {value_1} * {value_2} = {multiplication}")
print(f"Division: {value_1} / {value_2} = {division}")