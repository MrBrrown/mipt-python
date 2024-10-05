import random
import math
from decimal import Decimal

def solution1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    try:
        print("Result: ", a / b)
    except ZeroDivisionError as e:
        print(e.__class__.__name__, ": Cannot divide by zero")


def solution2():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result: ", a / b)
    except ValueError as e:
        print(e.__class__.__name__, ": Invalid input, ", e.args[0])
    except ZeroDivisionError as e:
        print(e.__class__.__name__, ": Cannot divide by zero")


class EvenException(Exception):
    pass
class NegativeException(Exception):
    pass


def solution3():
    list = [random.randint(-5,100) for i in range(10)]
    sum = 0
    
    for num in list:
        try:
            if num < 0:
                raise NegativeException("List contains negative number", num)
            elif num % 2 == 0:
                raise EvenException("List contains even number", num)
            else:
                sum += num
        except EvenException as e:
            print(e)
        except NegativeException as e:
            print(e)
    print("Sum of even numbers: ", sum)


def solution4(index: int):
    list = [random.randint(-5,100) for i in range(random.randint(5,22))]
    try:
        print(list[index])
    except IndexError as e:
        print(e)


def solution5():
    str_double = input("Enter a string: ")
    try:
        print(Decimal(str_double))
    except Exception as e:
        print(e)


def solution6(number: int):
    try:
        print(math.sqrt(number))
    except NameError as e:
        print(e)
    except ValueError as e:
        print(e)