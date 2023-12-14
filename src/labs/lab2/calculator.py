import math


class Calculator:
    def init(self):
        # Initialize the calculator with placeholders for values and operator.
        self.first_value = None
        self.operator = None
        self.second_value = None

    def run(self):
        while True:
            try:
                # Get user input and perform calculations.
                self.get_user_input()
                print("The result is", self.calculate())
            except Exception as e:
                # Handle exceptions and display error messages.
                print(str(e))

            response = input(
                "Would you like to continue? Enter 'Y' or 'y' if you do, or anything else if you do not. Your response is ").lower()
            if response != "y":
                break

    def get_user_input(self):
        # Get input from the user for the first value and operator.
        self.first_value = float(input("Enter the first value: "))
        self.operator = input("Enter the operator ['+', '-', '*', '/', '^', '√', '%']: ")

        if self.operator in ('+', '-', '*', '/', '^', '√', '%'):
            if self.operator != "√":
                # If the operator requires a second value, get it from the user.
                self.second_value = float(input("Enter the second value: "))
        else:
            # Raise a ValueError if the input operator is incorrect.
            raise ValueError("The input operator is incorrect")

    def calculate(self):
        # Perform calculations based on the operator chosen.
        if self.operator == "+":
            return self.first_value + self.second_value
        elif self.operator == "-":
            return self.first_value - self.second_value
        elif self.operator == "*":
            return self.first_value * self.second_value
        elif self.operator == "/":
            if self.second_value == 0:
                # Raise a ZeroDivisionError for division by zero.
                raise ZeroDivisionError("Impossible to divide")
            return self.first_value / self.second_value
        elif self.operator == "^":
            # Perform multiplication if the operator is an empty string.
            return self.first_value ** self.second_value
        elif self.operator == "√":
            if self.first_value < 0:
                # Raise a ValueError if trying to calculate the square root of a negative number.
                raise ValueError("Number is negative, therefore it is impossible to calculate the square root")
            return math.sqrt(self.first_value)
        elif self.operator == "%":
            # Calculate the remainder (modulo operation).
            return self.first_value % self.second_value


