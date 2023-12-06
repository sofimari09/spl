from calculator_operations import *
from console_interaction import *


history_of_calculations = []
decimal_places = 2


while True:
    print("Options: ")
    print("1. Add numbers (+)")
    print("2. Subtract numbers (-)")
    print("3. Multiply numbers (*)")
    print("4. Divide numbers (/)")
    print("5. Raise to a power (**)")
    print("6. Divide by modulo (%)")
    print("7. Compute the square root")
    print("8. View history")
    print("9. Open settings")
    print("0. Exit")

    input_value = input("Your option is ")

    if input_value in {"1", "2", "3", "4", "5", "6"}:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        try:
            operators = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "**", "6": "%"}
            operator = operators[input_value]
            operation_result = None

            if input_value == "1":
                operation_result = add(first_number, second_number)
            elif input_value == "2":
                operation_result = subtract(first_number, second_number)
            elif input_value == "3":
                operation_result = multiply(first_number, second_number)
            elif input_value == "4":
                operation_result = divide(first_number, second_number)
            elif input_value == "5":
                operation_result = raise_to_a_power(first_number, second_number)
            elif input_value == "6":
                operation_result = divide_by_modulo(first_number, second_number)

            history_of_calculations.append((f"{first_number} {operator} {second_number}", "=", operation_result))
            print("Result is {:.2f}\n".format(operation_result))
        except ZeroDivisionError as e:
            print(str(e) + "\n")
    elif input_value == "7":
        try:
            number = float(input("Enter number: "))
            result = compute_square_root(number)
            history_of_calculations.append(("√" + str(number), "=", result))
            print("Result is {:.2f}\n".format(result))
        except ArithmeticError as e:
            print(str(e) + "\n")
    elif input_value == "8":
        view_history(history_of_calculations)
        print()
    elif input_value == "9":
        while True:
            print("\tSettings options:")
            print("\t1. View settings")
            print("\t2. Change decimal places")
            print("\t3. Clean all records")
            print("\t0. Exit from the settings mode")

            inner_input_value = input("\tYour option is ")

            if inner_input_value == "1":
                view_settings(decimal_places)
                print()
            elif inner_input_value == "2":
                new_value = int(input("\tEnter a new value for decimal places: "))

                try:
                    decimal_places = change_decimal_places(new_value)
                    print()
                except ArithmeticError as e:
                    print("\t" + str(e) + "\n")
            elif inner_input_value == "3":
                history_of_calculations.clear()
                print()
            elif inner_input_value == "0":
                print()
                break
            else:
                print("\tYou have just entered a wrong option\n")
    elif input_value == "0":
        break
    else:
        print("You have just entered a wrong option\n")
