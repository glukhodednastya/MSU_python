from typing import List

"""
Подсчитать произведение ненулевых элементов на диагонали прямоугольной матрицы. 
Если ненулевых элементов на диагонали нет, то вернуть -1.
"""
def prod_non_zero_diag(X: List[List[int]]):
    prod = -1
    for i in range(min(len(X), len(X[0]))):
        if X[i][i] != 0:
            prod = abs(prod)
            prod *= X[i][i]
    return prod

"""
Даны два вектора x и y. Проверить, задают ли они одно и то же мультимножество.
"""
def are_multisets_equal(x: List[int], y: List[int]):
    return sorted(x) == sorted(y)

"""
 Найти максимальный элемент в векторе x среди элементов, перед которыми стоит нулевой. 
 Если нулевых элементов нет, то вернуть -1.
"""
def max_after_zero(x: List[int]):
    max = -1
    for i in range(1, len(x)):
        if (x[i-1] == 0):
            if x[i] > max:
                max = x[i]
    return max

"""
 Дан трёхмерный массив, содержащий изображение, размера (height, width, num_channels), 
 а также вектор весов длины num_channels. Сложить каналы изображения с указанными весами, 
 и вернуть результат в виде матрицы размера (height, width). 
"""
def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    sum = 0
    r = []
    res = []
    for i in range(len(image)):
        for j in range(len(image[i])):
            for k in range(len(image[i][j])):
                sum += image[i][j][k] * weights[k]
            r.append(sum)
            sum = 0
        res.append(r)
        r = []
    return res

"""
Реализовать кодирование длин серий (Run-length encoding). 
Для некоторого вектора x необходимо вернуть два вектора одинаковой длины. 
Первый содержит числа, а второй - сколько раз их нужно повторить.
"""
def run_length_encoding(x: List[int]) -> (List[int], List[int]):
    numbers = []
    countNumber = []
    k = x[0]
    f = 0
    count = 0
    for i in range(len(x)):
        if x[i] == k:
            f = x[i]
            count += 1
        else:
            k = x[i]
            numbers.append(f)
            f = x[i]
            countNumber.append(count)
            count = 1
    numbers.append(f)
    countNumber.append(count)
    return numbers, countNumber

"""
Даны две выборки объектов - X и Y. Вычислить матрицу евклидовых расстояний между объектами.
"""
from scipy.spatial.distance import cdist
def pairwise_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    return list(cdist(X, Y))