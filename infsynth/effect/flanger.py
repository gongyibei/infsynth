from ..signal import Analog, sinm


def basic_flanger(A, freq=1, depth=0.01, delay=0.001, wet=0.5):
    mod = sinm(freq) * depth + delay
    f = lambda t: A(t) * (1 - wet) + A(t - mod(t)) * wet
    return Analog(f)