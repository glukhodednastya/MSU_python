from typing import List

def prod_non_zero_diag(X: List[List[int]]):
    prod = -1
    for i in range(min(len(X), len(X[0]))):
        if X[i][i] != 0:
            prod = abs(prod)
            prod *= X[i][i]
    return prod

def are_multisets_equal(x: List[int], y: List[int]):
    return sorted(x) == sorted(y)

def max_after_zero(x: List[int]):
    max = -1
    for i in range(1, len(x)):
        if (x[i-1] == 0):
            if x[i] > max:
                max = x[i]
    return max

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

from scipy.spatial.distance import cdist
def pairwise_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    return list(cdist(X, Y))