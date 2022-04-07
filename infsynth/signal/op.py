import types

import numpy as np
import scipy.signal

from . import analog


# opperator warpper
def OP(opt):
    def wrapper(*args, **kwargs):
        O = analog.Analog()
        def oscillate(self, t): return opt(*args, **kwargs)(t)
        O.oscillate = types.MethodType(oscillate, O)
        return O
    return wrapper


@OP
def add(A, B):
    return lambda t: A(t) + B(t)


@OP
def sub(A, B):
    return lambda t: A(t) - B(t)


@OP
def mul(A, B):
    return lambda t: A(t) * B(t)


@OP
def lshift(A, dt):
    return lambda t: A(t + dt)


@OP
def rshift(A, dt):
    return lambda t: A(t - dt)


# I don't know when I'll need it either...
@OP
def conv(A, B):
    return lambda t: scipy.signal.convolve(A(t), B(t), mode='same')

# @OP
# def norm(A):
#     return


@OP
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
