from ..signal import Analog
from numpy import tan, cos, pi
from scipy.signal import lfilter


# First-order low-pass filter
def lpf(A, nf):
    wc = 2 * pi * nf
    b = [tan(wc / 2), tan(wc / 2)]
    a = [1 + tan(wc / 2), -(1 - tan(wc / 2))]
    f = lambda t: lfilter(b, a, A(t))
    return Analog(f)


# First-order high-pass filter
def hpf(A, nf):
    wc = 2 * pi * nf
    b = [1, -1]
    a = [1 + tan(wc / 2), -(1 - tan(wc / 2))]
    f = lambda t: lfilter(b, a, A(t))
    return Analog(f)


# First-order low-shelf filter
def lsf(A, nf, G):
    wc = 2 * pi * nf
    b = [1 + G * tan(wc / 2), -(1 - G * tan(wc / 2))]
    a = [1 + tan(wc / 2), -(1 - tan(wc / 2))]
    f = lambda t: lfilter(b, a, A(t))
    return Analog(f)


# First-order high-shelf filter
def hsf(A, nf, G):
    wc = 2 * pi * nf
    b = [tan(wc / 2) + G, tan(wc / 2) - G]
    a = [1 + tan(wc / 2), -(1 - tan(wc / 2))]
    f = lambda t: lfilter(b, a, A(t))
    return Analog(f)


# Second-order band-pass filter
def bpf(A, nf, bw):
    wc = 2 * pi * nf
    B = 2 * pi * bw
    b = [tan(B / 2), 0, -tan(B / 2)]
    a = [1 + tan(B / 2), -2 * cos(wc), 1 - tan(B / 2)]
    f = lambda t: lfilter(b, a, A(t))
    return Analog(f)


# Second-order band-stop filter
def bsf(A, nf, bw):
    wc = 2 * pi * nf
    B = 2 * pi * bw
    b = [1, -2 * cos(wc), 1]
    a = [1 + tan(B / 2), -2 * cos(wc), 1 - tan(B / 2)]
    f = lambda t: lfilter(b, a, A(t))
    return Analog(f)


# Peaking or notch filter
def pnf(A, nf, bw, G):
    wc = 2 * pi * nf
    B = 2 * pi * bw
    b = [1 + G * tan(B / 2), -2 * cos(wc), 1 - G * tan(B / 2)]
    a = [1 + tan(B / 2), -2 * cos(wc), 1 - tan(B / 2)]
    f = lambda t: lfilter(b, a, A(t))
    return Analog(f)