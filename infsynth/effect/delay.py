from ..signal import analog_warpper

@analog_warpper
def basic_delay(A, delay_time, decay=0.5):
    return lambda t: A(t) + A(t - delay_time) * decay