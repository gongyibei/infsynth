from ..signal import analog_warpper, sinm


@analog_warpper
def basic_flanger(A, freq=1, depth=0.01, delay=0.001, wet=0.5):
    mod = sinm(freq) * depth + delay
    return lambda t: A(t) * (1 - wet) + A(t - mod(t)) * wet