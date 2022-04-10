import numpy as np


class Module(object):

    def __init__(self):
        self.sample_rate = 44100
        self.buf_size = 2048
        self.dtype = np.float32

    def forward(self):
        raise NotImplementedError("Derived classes must override this method")

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
