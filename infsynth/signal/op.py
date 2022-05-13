import numpy as np
import scipy.signal
from sklearn.linear_model import lasso_path
from .analog import Analog
from .basic import dc, sampler
import random


def add(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) + B(t), max(A.T, B.T))


def sub(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) - B(t), max(A.T, B.T))


def mul(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) * B(t), max(A.T, B.T))


def div(A, B):
    if type(A) == int or type(A) == float:
        A = dc(A)
    if type(B) == int or type(B) == float:
        B = dc(B)
    return Analog(lambda t: A(t) / B(t), max(A.T, B.T))


def lshift(A, dt):
    return Analog(lambda t: A(t + dt), A.T)


def rshift(A, dt):
    return Analog(lambda t: A(t - dt), A.T)


def conv(A, kernel):
    return Analog(lambda t: scipy.signal.convolve(A(t), kernel, mode='same'),
                  A.T)


def con(analog_list, duration_list=None):
    if duration_list is None:
        duration_list = [a.T for a in analog_list]

    T = sum(duration_list)

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

    return Analog(f, T)


def cut(A, t1, t2):
    assert t2 > t1

    def f(t):
        t = t % (t2 - t1)
        return (A << t1)(t)

    return Analog(f, t2 - t1)


def rev(A):
    return Analog(lambda t:A(A.T - t), A.T)

def norm(A):
    return Analog(lambda t: A(t) / (max(abs(A(t))) + 1e-9), A.T)


def freeze(A, minT=10e-6, maxT=1000, sr=44100):
    if A.T > maxT:
        raise "the T of the signal is too long!"
    if A.T < minT:
        raise "the T of the signal is too short!"
    arr = A(np.arange(0, A.T, 1/sr))
    return sampler(arr, sr)


def imp(A, seq='1', on='1', off='0'):
    O = dc(0)
    seq = ''.join([s for s in seq if s in [on, off]])
    L = len(seq)
    for i, s in enumerate(seq):
        if s == on:
            O += A >> (i / L * A.T)
    return O


def seq(analog_list, seq=None, on=None, off='-', rnd='?'):
    if on is None:
        assert len(analog_list) < 16
        on = '123456789abcdef'[:len(analog_list)]
    else:
        assert len(analog_list) == len(on)

    on = list(on)
    all_sym = on + [off] + [rnd]
    if seq is None:
        seq = on
    
    O = dc(0)
    seq = [s for s in seq if s in all_sym]
    L = len(seq)
    for i, s in enumerate(seq):
        if s in on: 
            A = analog_list[on.index(s)]
            O += A >> (i / L * A.T)
        if s == rnd:
            A = random.choice(analog_list)
            O += A >> (i / L * A.T)
    return O