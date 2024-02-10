
# Flowchart for the calculator program

# Start
print("Welcome to the Calculator!")

# Get the first number
num1 = float(input("Enter the first number: "))

# Display the available operations
print("* \n/ \n- \n+")

# Get the selected operation
selected_operation = input("Pick an operation from above: ")

# Get the second number
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the selected operation
if selected_operation in operations:
    result = operations[selected_operation](num1, num2)
    if result is not None:
        print(f"{num1} {selected_operation} {num2} = {result}")
else:
    print("Invalid operation selected.")

# Loop to continue calculating
while True:
    continue_calc = input(
        'Type "y" to continue calculating with the result, "n" to start a new calculation, or "stop" to exit: '
    )
    if continue_calc == "n":
        result = calculate()
    elif continue_calc == "y" and result is not None:
        selected_operation = input("Pick an operation: ")
        num = float(input("Enter the second number: "))
        if selected_operation in operations:
            result = operations[selected_operation](result, num)
            if result is not None:
                print(f"{result}")
        else:
            print("Invalid operation!")
    elif continue_calc == "stop":
        break
    else:
        print("Invalid input!")

# End
---------------------------------------------------------------------------------

This flowchart outlines the steps of the calculator program:

1. **Start**: Display a welcome message.
2. Get the first number from the user.
3. Display the available operations: `*`, `/`, `-`, `+`.
4. Get the selected operation from the user.
5. Get the second number from the user.
6. Perform the calculation based on the selected operation.
7. Loop to continue calculating:
   - If the user wants to continue with the result, get a new operation and number.
   - If the user wants to start a new calculation, repeat steps 2-6.
   - If the user wants to stop, exit the
