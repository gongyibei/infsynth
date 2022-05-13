from .module import Module
import numpy as np

class Oscillator(Module):
    def __init__(self, A):
        super().__init__()
        self.idx = 0
        self.analog = A
    
    def forward(self, gate):
        if gate == 0:
            self.idx = 0
            return np.repeat(0, self.buf_size)
        else:
            t = np.arange(self.idx, self.idx + self.buf_size) / self.sample_rate
            self.idx += self.buf_size
            return self.analog(t)
