from ctypes import Union
from re import U
import numpy as np
import scipy.signal
import scipy.integrate
import scipy.io.wavfile as wav

from .analog import Analog


def sin(freq, phase=0):

    def f(t):
        if type(freq) == int or type(freq) == float:
            phase_t = freq * t
        elif type(freq) == Analog:
            phase_t = scipy.integrate.cumulative_trapezoid(freq(t),
                                                           t,
                                                           initial=0)
        else:
            raise "Unsupported type of freq"
        return np.sin(2 * np.pi * phase_t + phase)

    return Analog(f)


def squ(freq, duty=0.5, phase=0):

    def f(t):
        if type(freq) == int or type(freq) == float:
            phase_t = freq * t
        elif type(freq) == Analog:
            phase_t = scipy.integrate.cumulative_trapezoid(freq(t),
                                                           t,
                                                           initial=0)
        else:
            raise "Unsupported type of freq"
        return scipy.signal.square(2 * np.pi * phase_t + phase, duty=duty)

    return Analog(f)


def saw(freq, width=0, phase=0):

    def f(t):
        if type(freq) == int or type(freq) == float:
            phase_t = freq * t
        elif type(freq) == Analog:
            phase_t = scipy.integrate.cumulative_trapezoid(freq(t),
                                                           t,
                                                           initial=0)
        else:
            raise "Unsupported type of freq"
        return scipy.signal.sawtooth(2 * np.pi * phase_t + phase, width=width)

    return Analog(f)


def freeze(freq, width=0, phase=0):
    pass


def dc(value):
    return Analog(lambda t: value)


def sampler(arr, fs):
    T = (len(arr) - 1) / fs
    y = arr
    x = np.arange(len(arr)) / fs
    f = lambda t: scipy.interpolate.interp1d(x, y)(t % T)
    return Analog(f)


def fromfile(file_name):
    fs, data = wav.read(file_name)
    return sampler(data, fs)
