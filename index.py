import art
# 0. Write out the functions - add, subtract, multiply and divide.
def add(n1, n2):
    return n1 + n2

# add_operation = add


# Subtraction function
def subtract(n1, n2):
    return n1 - n2

# subtraction_operation = subtract
# print(subtraction_operation(10, 3))

# multiply function
def multiply(n1, n2):
    return n1 * n2

# multiplication_operation =  multiply
# print(multiplication_operation(5, 3))

# division function
def divide(n1, n2):
    return n1 / n2

# division_operation =  divide
# print(division_operation(20, 4))

#Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# 8.(b) If no, program asks the user for the fist number again and wipes all memory of previous calculations.
def calculator():
    print(art.logo1)
    # 7.(a.2) If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    should_accumulate = True
    # 1. Program asks the user to type the first number.
    num1 = float(input("What is your first number?:\n"))
    # 7.(b) If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    while should_accumulate:
        # 3. Program works out the result based on the chosen mathematical operator.
        for symbol in operations:
            print(symbol)
        # 2. Program asks the user to type a mathematical operator.
        operator_symbol = input("Type one of the above operators: ( +  -  *  or / )\n")
        # 4. Program asks the user to type the second number.
        num2 = float(input("What is your next number?:\n"))
        # 5. Program works out the result based on the chosen mathematical operator.
        answer = operations[operator_symbol](num1, num2)
        print(f"{num1} {operator_symbol} {num2} = {answer}")

        # 6.(a) Program asks if the user wants to continue working with the previous result.
        choice = input(f"Type 'y' to continue operating with the previous result: '{answer}'or type 'n' to start a new calculation.\n").lower()
        # 7.(a.1) If yes, program loops to use the previous result as the first number and then repeats the calculation process.
        if choice == "y":
            num1 = answer
        else:
            # 8.(a) If no, program asks the user for the fist number again and wipes all memory of previous calculations.
            should_accumulate = False
            print("\n" * 100)
            # 8.(c) If no, program asks the user for the fist number again and wipes all memory of previous calculations.
            calculator()

# 8.(d) If no, program asks the user for the fist number again and wipes all memory of previous calculations.
calculator()





























































