__author__ = 'Ana Paula de Souza Nalli - 2022101124'

from general import list_of_primes
from general import is_prime
from general import quadratic_euler


a_max: int = 0
b_max: int = 0
n_max: int = 0
consecutive_primes = []  # extra info

n_primes: list = list_of_primes(10 ** 4)

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n: int = 0
        n_list = []  # extra info
        while is_prime((p := quadratic_euler(a, b, n)), n_primes):
            # p = quadratic_euler(a, b, n)
            n += 1
            n_list.append(p)  # extra info
        if n > n_max:
            a_max = a
            b_max = b
            n_max = n
            consecutive_primes.clear()  # extra info
            consecutive_primes = n_list.copy()  # extra info

print(f'O produto dos coeficientes vale {a_max * b_max}')

# Extra info:
print(f'O número máximo de primos consecutivos foi: {n_max}')
print(f'O coeficiente a vale {a_max}')
print(f'O coeficiente b vale {b_max}')
for x, y in enumerate(consecutive_primes):
    print(f'When n = {x}, the formula "n² + an + b" generates {y}')
