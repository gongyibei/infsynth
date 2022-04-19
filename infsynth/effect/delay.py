from ..signal import Analog

def basic_delay(A, delay_time, decay=0.5):
    f = lambda t: A(t) + A(t - delay_time) * decay
    return Analog(f)