import numpy as np
import scipy.signal
from .analog import Analog
from .basic import dc


def add(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) + B(t))


def sub(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) - B(t))


def mul(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) * B(t))


def div(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) / B(t))


def lshift(A, dt):
    return Analog(lambda t: A(t + dt))


def rshift(A, dt):
    return Analog(lambda t: A(t - dt))


def conv(A, kernel):
    return Analog(lambda t: scipy.signal.convolve(A(t), kernel, mode='same'))


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

        return np.piecewise(t, condlist, funclist)

    return Analog(f)


def norm(A):
    return Analog(lambda t: A(t) / (max(abs(A(t))) + 1e-9))


def freeze(A):
    pass


def imp(A, seq='1', T=1, on='1', off='0'):
    O = dc(0)
    seq = ''.join([s for s in seq if s in [on, off]])
    L = len(seq)
    for i, s in enumerate(seq):
        if s == on:
            O += A >> (i / L * T)
    return O


def seq(op, param, T=0.2):
    concat(list(map(op, param)), [T] * len(param))
