import math


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Impossible to divide")
    return num1 / num2


def raise_to_a_power(num1, num2):
    return num1 ** num2


def compute_square_root(num):
    if num < 0:
        raise ArithmeticError("Number is negative, therefore it is impossible to calculate the square root")
    return math.sqrt(num)


def divide_by_modulo(num1, num2):
    return num1 % num2
