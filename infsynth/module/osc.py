from .module import Module

class Oscillator(Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, freq):
        pass

class Sin(Oscillator):
    def __init__(self):
        super().__init__()


class Squ(Oscillator):
    def __init__(self):
        super().__init__()

class Saw(Oscillator):
    def __init__(self):
        super().__init__()