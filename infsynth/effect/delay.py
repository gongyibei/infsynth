from numpy import sign
from ..signal import signal_warpper

@signal_warpper
def delay(A, delay_time, decay=0.5):
    return lambda t: A(t) + A(t - delay_time) * decay