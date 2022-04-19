import math
from .analog import Analog
from .basic import sin, squ, saw, dc
from . import op


# sin modulation
def sinm(freq):
    return (sin(freq) + 1.) * 0.5


# square modulation
def squm(freq):
    return (squ(freq) + 1.) * 0.5


# sawtooth modulation
def sawm(freq):
    return (saw(freq) + 1.) * 0.5


def attack(duration, power=0.5):
    power = min(max(power, 1e-6), 1)
    exp = -math.log2(power)
    f = lambda t: ((t % duration) / duration)**exp
    return Analog(f)


def decay(duration, power=0.5):
    power = min(max(power, 1e-6), 1)
    exp = -math.log2(power)
    f = lambda t: (1 - (t % duration) / duration)**exp
    return Analog(f)


def sustain(value):
    f = lambda t: value
    return Analog(f)


def release(duration, power=0.5):
    power = min(max(power, 1e-6), 1)
    exp = -math.log2(power)
    f = lambda t: (1 - (t % duration) / duration)**exp
    return Analog(f)


def adsr(a=[0.01, 0.5],
         d=[0.05, 0.3],
         s=[0.05, 0.5],
         r=[0.5, 0.2]):
    att = attack(*a)
    dec = decay(*d) * (1 - s[1]) + s[1]
    sus = sustain(s[1])
    rel = release(*r) * s[1]
    return op.concat([att, dec, sus, rel],
                     [a[0], d[0], s[0], r[0]])


def ad(a=[0.01, 0.5], d=[0.1, 0.5]):
    att = attack(*a)
    dec = decay(*d)
    return op.concat([att, dec], [a[0], d[0]])
