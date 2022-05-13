from .sink import PaSink
from .source import KeyboardSource
from .osc import Oscillator
from .module import Module

class MonoKeySynth(Module):
    def __init__(self, key, Analog):
        Module.__init__(self)
        self.osc = Oscillator(Analog)
        self.keyboard = KeyboardSource(key)
        self.sink = PaSink()

    def forward(self):
        gate = self.keyboard()
        X = self.osc(gate)
        return X, gate

class PolyKeySynth(Module):
    def __init__(self, mapping):
        Module.__init__(self)
        self.monosynth_list = []
        for key, analog, in mapping.items():
            self.monosynth_list.append(
                MonoKeySynth(key, analog))
        self.sink = PaSink()

    def forward(self):
        X = []
        for synth in self.monosynth_list:
            tmp, gate = synth()
            X.append(tmp)
        X = sum(X) / 6
        self.sink(X)

    def start(self):
        while True:
            self()

