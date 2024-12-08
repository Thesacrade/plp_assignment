result = 0
try:
    first_number = int(input("Enter the first number "))
    second_number = int(input("Enter the second number "))
    operator = input("Enter the operation to be done ")
    if operator == "-":
        result = first_number - second_number
    elif operator == "+":
        result = first_number + second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    elif operator == "%":
        result = first_number % second_number
    else:
        print("enter a valid number and operator")

    print(f" Answer is: {result}")
except Exception as e:
    print(f"A {e} error occurred in your program")

