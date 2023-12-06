def view_history(history):
    if not history:
        print("There is nothing in history")
    else:
        print("History of results:")
        for calculation in history:
            operands, operator, result = calculation
            print(f"{operands} {operator} = {result:.2f}")


def view_settings(decimal_places):
    print("\tSettings:")
    print("\tDecimal places are " + str(decimal_places))


def change_decimal_places(value):
    if value <= 0:
        raise ArithmeticError("Decimal digits can't be negative or 0")
    return value
