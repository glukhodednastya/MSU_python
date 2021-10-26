import numpy as np

"""
Подсчитать произведение ненулевых элементов на диагонали прямоугольной матрицы. 
Если ненулевых элементов на диагонали нет, то вернуть -1.
"""
def prod_non_zero_diag(X: np.ndarray):
    prod = -1
    prod *= np.prod(np.diag(X)[np.diag(X) != 0])
    if prod == -1:
        return -1
    return abs(prod)

"""
Даны два вектора x и y. Проверить, задают ли они одно и то же мультимножество.
"""
def are_multisets_equal(x: np.ndarray, y: np.ndarray):
    return np.array_equal(np.sort(x), np.sort(y))

"""
 Найти максимальный элемент в векторе x среди элементов, перед которыми стоит нулевой. 
 Если нулевых элементов нет, то вернуть -1.
"""
def max_after_zero(x: np.ndarray):
    zero = (x == 0)
    if np.all(x != 0):
        return -1
    zero = np.insert(zero, 0, False)
    x = np.append(x, -1)
    res = x[zero].max()
    return res

"""
 Дан трёхмерный массив, содержащий изображение, размера (height, width, num_channels), 
 а также вектор весов длины num_channels. Сложить каналы изображения с указанными весами, 
 и вернуть результат в виде матрицы размера (height, width). 
"""
def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return image.dot(weights)

"""
Реализовать кодирование длин серий (Run-length encoding). 
Для некоторого вектора x необходимо вернуть два вектора одинаковой длины. 
Первый содержит числа, а второй - сколько раз их нужно повторить.
"""
def run_length_encoding(x: np.ndarray) -> (np.ndarray, np.ndarray):
    x = np.asanyarray(x)
    n = x.shape[0]
    if n == 0:
        return np.array([]), np.array([])
    else:
        loc_run_start = np.empty(n, dtype=bool)
        loc_run_start[0] = True
        np.not_equal(x[:-1], x[1:], out=loc_run_start[1:])
        run_starts = np.nonzero(loc_run_start)[0]
        run_values = x[loc_run_start]
        run_lengths = np.diff(np.append(run_starts, n))
        return run_values, run_lengths

"""
Даны две выборки объектов - X и Y. Вычислить матрицу евклидовых расстояний между объектами.
"""
def pairwise_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return np.sqrt(np.add.outer(np.sum(X ** 2, axis=1), np.sum(Y ** 2, axis=1)) - 2 * np.dot(X, Y.T))
