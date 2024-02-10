from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    else:
        return a / b


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate():
    num1 = float(input("Enter the first number: "))
    print("* \n/ \n- \n+")
    selected_operation = input("Pick an operation from above: ")
    num2 = float(input("Enter the second number: "))


    if selected_operation in operations:
        result = operations[selected_operation](num1, num2)
        if result is not None:
            print(f"{num1} {selected_operation} {num2} = {result}")
            return result
    else:
        print("Invalid operation selected.")
        return None


print(logo)

result = calculate()

while True:
    continue_calc = input(
        'Type "y" to continue calculating with the result, "n" to start a new calculation, or "stop" to exit: '
    )
    if continue_calc == "n":
        result = calculate()
    elif continue_calc == "y" and result is not None:
        selected_operation = input("Pick an operation: ")
        num = float(input("Enter a the second number: "))
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
