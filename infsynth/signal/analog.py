import types
from . import op


class Analog(object):

    def __init__(self, f):
        self._call = f

    def __call__(self, t):
        return self._call(t)

    # Mix two signal
    def __add__(self, X):
        return op.add(self, X)

    def __sub__(self, X):
        return op.sub(self, X)

    # Modulation signal with X
    def __mul__(self, X):
        return op.mul(self, X)

    def __truediv__(self, X):
        return op.div(self, X)

    # Emmmm, How to say...
    def __lshift__(self, dt):
        return op.lshift(self, dt)

    # Delay signal
    def __rshift__(self, dt):
        return op.rshift(self, dt)

    # Mix two signal
    def add(self, X):
        return op.add(self, X)

    # Modulation signal with X
    def mul(self, X):
        return op.mul(self, X)

    # Emmmm, How to say...
    def lshift(self, dt):
        return op.lshift(self, dt)

    # Delay signal
    def rshift(self, dt):
        return op.rshift(self, dt)

    def conv(self, X):
        return op.conv(self, X)