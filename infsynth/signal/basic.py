from ctypes import Union
from re import U
import numpy as np
import scipy.signal

from .analog import analog_warpper


@analog_warpper
def sin(freq, amp = 1, phase = 0):
    return lambda t: np.sin(2 * np.pi * freq * t + phase) * amp

@analog_warpper
def squ(freq, duty = 0.5):
    return lambda t: scipy.signal.square(2 * np.pi * freq * t, duty=duty)

@analog_warpper
def saw(freq, width = 0.5):
    return lambda t: scipy.signal.sawtooth(2 * np.pi * freq * t, width=width)

@analog_warpper
def dc(value):
    return lambda t: value
    

@analog_warpper
def sampler(arr, sr):
    return lambda t: arr[int(t * sr)]