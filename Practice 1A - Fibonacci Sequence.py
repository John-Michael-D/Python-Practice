#Fibonacci Sequence:
#The sum of two elements defines the next.

a, b = 0, 1 #Establishes the initial values of the sequence.
iteration_count = 0 #Initializes the increment counter.

while a < 9000:
    print(a, f"(Fibonacci Sequence Iteration = {iteration_count}.)")
    a, b = b, a+b
    iteration_count += 1 #Increases the counter by 1 with each iteration of the while loop.