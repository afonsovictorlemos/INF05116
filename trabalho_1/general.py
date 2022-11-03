"""
All functions must be here.
"""


def reversed_number(arg: int) -> int:
    arg: str = str(arg)  # Changing int into str
    arg: str = arg[::-1]  # Reversing str
    arg: int = int(arg)  # Changing str into int
    return arg  # return int(str(arg).__reversed__)


def is_palindrome(arg: int) -> bool:
    par: int = reversed_number(arg)
    return arg == par


def is_prime(n: int, p: list) -> bool:
    """
    It checks if a 'n' number is in the 'p' list of prime numbers.
    :param n: int
    :param p: list
    :return: bool
    """
    for x in p:
        q: int = n // x
        if x >= q:  # x * q = n = q * x
            return True
        elif n % x == 0:
            return False
    return True  # If the list is empty, then the number is prime


def list_of_primes(arg: int) -> list:
    primes: list = []
    for i in range(2, arg):
        if is_prime(i, primes):
            primes.append(i)
    return primes


def quadratic_euler(x: int, y: int, z: int) -> int:
    number: int = z ** 2 + x * z + y  # n^2 + an + b
    number: int = abs(number)
    return number
