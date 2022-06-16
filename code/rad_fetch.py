##### imports
import numpy as np
import math

##### Definitions

def _func(a, b):
    if [a, b] == [1., 1.]:
        return 0.
    if [a, b] == [-1., 1.] or [a, b] == [-1., -1.]:
        return math.pi
    if [a, b] == [1., -1.]:
        return 2 * math.pi

vfun = np.vectorize(_func)

def rthetas(x, c):
    '''
    :param x: numpy array of shape (n, 2). Each element contain as coordinate (x, y)
    :param c: numpy array of shape (2, 1). Center as (c1, c2)
    :return: numpy array of shape (n, 2). Returns (r, theta). i.e. this function transforms (x, y)->(r, theta).
    '''
    y = (x - c)[(x - c)[:, 0] != 0]
    y = y[y[:, 1] != 0]
    r = np.sqrt(y.T[:1].T ** 2 + y.T[1:].T ** 2)
    sign = y / np.abs(y)

    shifts = vfun(*sign.T).reshape(sign.shape[0], 1)
    theta = np.arctan(y.T[1:].T / y.T[:1].T) + shifts
    return np.array([theta, r]).T.reshape(-1, 2)









