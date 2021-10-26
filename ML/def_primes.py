"""
Требуется реализовать функцию-генератор primes(),
которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
"""
import itertools

def primes():
    lst = []
    for i in itertools.count(2, 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i