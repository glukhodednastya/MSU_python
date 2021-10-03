"""
Требуется написать функцию is_palindrome(x),
принимающую целое положительное число и проверить, является ли оно палиндромом.
Представлять число в виде последовательности (строки, списка и т. п.) нельзя.
"""
import math

def is_palindrome(x):
    first = 0
    last = 0
    if x != 0:
        last = int(math.log10(x))
    if last == 0:
        return 'YES'
    else:
        while last > first:
            if x // 10 ** first % 10 == x // 10 ** last % 10:
                first += 1
                last -= 1
            else:
                return 'NO'
        return 'YES'