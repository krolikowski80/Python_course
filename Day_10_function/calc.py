# kalkulator
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


should_continue = True
while should_continue:
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    for symol in operations:
        print(symol)
    operations_symbol = input("Enter operation symbol from line above: ")
    callulation_function = operations[operations_symbol]
    answer = callulation_function(num1, num2)
    print(f"Answer: {num1} {operations_symbol} {num2} = {answer}")
    if input("Continue? (y/n): ").lower() == "y":
        should_continue = True
    else:
        should_continue = False
