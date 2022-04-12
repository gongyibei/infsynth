from ctypes import Union
from re import U
import numpy as np
import scipy.signal
import scipy.integrate
import scipy.io.wavfile as wav

from .analog import analog_warpper, Analog


@analog_warpper
def sin(freq, phase = 0):
    def f(t):
        if type(freq) == int or type(freq) == float:
            phase_t = freq * t
        elif type(freq) == Analog:
            phase_t = scipy.integrate.cumulative_trapezoid(freq(t), t, initial=0)
        else:
            raise "Unsupported type of freq"
        return np.sin(2 * np.pi * phase_t  + phase)
    return f

@analog_warpper
def squ(freq, duty = 0.5, phase = 0):
    def f(t):
        if type(freq) == int or type(freq) == float:
            phase_t = freq * t
        elif type(freq) == Analog:
            phase_t = scipy.integrate.cumulative_trapezoid(freq(t), t, initial=0)
        else:
            raise "Unsupported type of freq"
        return scipy.signal.square(2 * np.pi * phase_t  + phase, duty=duty)
    return f


@analog_warpper
def saw(freq, width = 0, phase = 0):
    def f(t):
        if type(freq) == int or type(freq) == float:
            phase_t = freq * t
        elif type(freq) == Analog:
            phase_t = scipy.integrate.cumulative_trapezoid(freq(t), t, initial=0)
        else:
            raise "Unsupported type of freq"
        return scipy.signal.sawtooth(2 * np.pi * phase_t  + phase, width=width)
    return f

@analog_warpper
def dc(value):
    return lambda t: value
    

@analog_warpper
def sampler(arr, fs, freq=None):
    if freq:
        T = 1/freq
    else:
        T = (len(arr)-1)/fs
    np.pad(arr, (0, max(0, int(T*fs) - len(arr) + 1)))
    return lambda t: scipy.interpolate.interp1d(np.arange(len(arr))/fs, arr)(t%T)

def fromfile(file_name):
    fs, data = wav.read(file_name)
    return sampler(data, fs)
    
    