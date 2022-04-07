import numpy as np
import scipy.signal

from .analog import AC, DC


class Sin(AC):

    def __init__(self, freq):
        AC.__init__(self, freq)

    def oscillate(self, t):
        return np.sin(2 * np.pi * (1 / self.T) * t)


class Square(AC):

    def __init__(self, freq, duty=DC(0.5)):
        AC.__init__(self, freq)
        self.duty = duty

    def oscillate(self, t):
        return scipy.signal.square(2 * np.pi * (1 / self.T) * t,
                                   duty=self.duty.v)


class Saw(AC):

    def __init__(self, freq, width=DC(0.5)):
        AC.__init__(self, freq)
        self.width = width

    def oscillate(self, t):
        return scipy.signal.sawtooth(2 * np.pi * (1 / self.T) * t,
                                     width=self.width.v)
