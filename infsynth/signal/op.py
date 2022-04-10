import numpy as np
import scipy.signal
from .analog import analog_warpper


@analog_warpper
def add(A, B):
    if type(B) == int or type(B) == float:
        return lambda t: A(t) + B
    else:
        return lambda t: A(t) + B(t)


@analog_warpper
def sub(A, B):
    if type(B) == int or type(B) == float:
        return lambda t: A(t) - B
    else:
        return lambda t: A(t) - B(t)


@analog_warpper
def mul(A, B):
    if type(B) == int or type(B) == float:
        return lambda t: A(t) * B
    else:
        return lambda t: A(t) * B(t)


@analog_warpper
def lshift(A, dt):
    return lambda t: A(t + dt)


@analog_warpper
def rshift(A, dt):
    return lambda t: A(t - dt)


# I don't know when I'll need it either...
@analog_warpper
def conv(A, B):
    return lambda t: scipy.signal.convolve(A(t), B(t), mode='same')


@analog_warpper
def concat(analog_list, duration_list):
    def f(t):
        t = t % sum(duration_list)
        condlist = []
        funclist = []
        last = cur = 0
        for A, duration in zip(analog_list, duration_list):
            cur += duration
            condlist.append((t >= last) & (t < cur))
            funclist.append(A >> last)
            last = cur

        return np.piecewise(
            t,
            condlist,
            funclist
        )
    return f

# @analog_warpper
# def norm(A):
#     return
