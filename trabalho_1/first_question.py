__author__ = 'Afonso Victor Lemos da Silva'

from general import is_prime
from general import is_palindrome
from general import reversed_number

from math import pow
from math import sqrt

primes: list = []
square_primes: list = []
exp: int = 0
limit: int = 10

while len(square_primes) < limit:
    exp += 1
    n_start: int = 10 ** (exp - 1) + 1
    n_end: int = 10 ** exp
    for n in range(n_start, n_end):
        if is_prime(n, primes):
            primes.append(n)
    selected_primes: list = []  # discarding prime numbers less than n_start
    for prime in primes:
        if prime < n_start:
            continue
        else:
            selected_primes.append(prime)
    for prime in selected_primes:
        square_prime: int = int(pow(prime, 2))
        if is_palindrome(square_prime):
            continue  # next iteration, square_prime number must not be palindrome
        reversed_square: int = reversed_number(square_prime)
        reversed_rooted: float = sqrt(reversed_square)
        if reversed_rooted % 1.0 != 0.0:
            continue  # next iteration, reversed_rooted module is different from 0.0
        reversed_rooted: int = int(reversed_rooted)
        if reversed_rooted in selected_primes:
            square_primes.append(square_prime)
            if len(square_primes) == limit:
                break  # break this loop, prevents to add more elements to square_primes

# print(sum(square_primes))
square_prime_sum = 0
for x in square_primes:
    square_prime_sum += x
print(f'A soma dos quadrados primos reversíveis vale: {square_prime_sum}')

# print(square_primes)
for x, y in enumerate(square_primes, start=1):
    print(f'O {x}º elemento é: {y}')
