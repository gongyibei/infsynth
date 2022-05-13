import numpy as np

import pyaudio

from .module import Module


class PaSink(Module):

    def __init__(self):
        Module.__init__(self)
        self.stream = self._init_stream()

    def _init_stream(self, nchannels=1):
        return pyaudio.PyAudio().open(rate=self.sample_rate,
                                      channels=nchannels,
                                      format=pyaudio.paInt16,
                                      output=True,
                                      frames_per_buffer=self.buf_size)

    def forward(self, X):
        X = (X * 32768).astype(np.int16)
        self.stream.write(X.tobytes())