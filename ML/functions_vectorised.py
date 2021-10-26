import numpy as np

def prod_non_zero_diag(X: np.ndarray):
    prod = -1
    prod *= np.prod(np.diag(X)[np.diag(X) != 0])
    if prod == -1:
        return -1
    return abs(prod)

def are_multisets_equal(x: np.ndarray, y: np.ndarray):
    return np.array_equal(np.sort(x), np.sort(y))

def max_after_zero(x: np.ndarray):
    zero = (x == 0)
    if np.all(x != 0):
        return -1
    zero = np.insert(zero, 0, False)
    x = np.append(x, -1)
    res = x[zero].max()
    return res

def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return image.dot(weights)

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

def pairwise_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return np.sqrt(np.add.outer(np.sum(X ** 2, axis=1), np.sum(Y ** 2, axis=1)) - 2 * np.dot(X, Y.T))
