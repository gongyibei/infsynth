import types

import numpy as np

from . import op


class Analog(object):

    def __init__(self):
        pass

    def __call__(self, t):
        return self.oscillate(t)

    def oscillate(self, t):
        return 0

    # Mix two signal
    def __add__(self, X):
        return op.add(self, X)

    # Modulation signal with X
    def __mul__(self, X):
        return op.mul(self, X)

    # Emmmm, How to say...
    def __lshift__(self, dt):
        return op.lshift(self, dt)

    # Delay signal
    def __rshift__(self, dt):
        return op.rshift(self, dt)

    def __call__(self, t):
        return self.oscillate(t)

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


# Direct Current
class DC(Analog):

    def __init__(self, v):
        Analog.__init__(self)
        self.v = v

    def oscillate(self, t):
        return np.repeat(self.v, len(t))


# Alternating Current
class AC(Analog):

    def __init__(self, freq):
        Analog.__init__(self)
        self.T = 1 / freq
