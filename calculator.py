from art import logo
# add
def add(a1, a2):
    return a1 + a2

# subtract

def subtract(a1, a2):
    return a1 - a2

# multiply

def multiply(a1, a2):
    return a1 * a2

# divide

def divide(a1, a2):
    return a1 / a2

operations = { 
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    print(logo)
    num1 = float(input("what is first number?"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation:")
        num2 = float(input("what is next number?"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue the calculation{answer} or type 'n' to start new calculation") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()