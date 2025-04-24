import operator


def add(x, y): return operator.add(x, y)


def subtract(x, y): return operator.sub(x, y)


def multiply(x, y): return operator.mul(x, y)


def divide(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero")
    return operator.truediv(x, y)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate():
    print("Simple Calculator Application Using Python")
    print("Enter quit to exit")

    while True:
        expression = input("\n Enter calculation (e.g. 2 + 2) : ")
        if expression.lower() == "quit":
            print("Exiting. Good Bye !!!")
            break
        parts = expression.split()
        if len(parts) != 3:
            print("\n Invalid format: Use 'Number Operator Number'")
            continue
        num1, optr, num2 = parts
        if optr not in operations:
            print(f"\n Unsupported operator '{optr}'. Valid Operators: {','.join(operations.keys())}")
            continue
        try:
            x = float(num1)
            y = float(num2)
            result = operations[optr](x, y)
            print(f"\n Result: {result}")
        except ValueError as ve:
            print(f"\n Error: {ve}")
        except Exception:
            print(f"\n Error occurred. Try again")


if __name__ == '__main__':
    calculate()
