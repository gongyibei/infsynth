from . import op

class Analog(object):
    sample_rate = 44100

    def __init__(self, f, T=float('inf')):
        self._call = f
        self.T = T

    # sampling
    def __call__(self, t):
        return self._call(t)

    # Mix two signal
    def __add__(self, X):
        return op.add(self, X)

    def __sub__(self, X):
        return op.sub(self, X)

    # Modulation signal with X
    def __mul__(self, X):
        return op.mul(self, X)

    def __truediv__(self, X):
        return op.div(self, X)

    # Emmmm, How to say...
    def __lshift__(self, dt):
        return op.lshift(self, dt)

    # Delay signal
    def __rshift__(self, dt):
        return op.rshift(self, dt)
    
    # Concat signal with signal B
    def __or__(self, B):
        return op.con([self, B])
    
    def __getitem__(self, slice):
        pass


    # Mix two signal
    def add(self, X):
        return op.add(self, X)

    # Modulation signal with X
    def mul(self, X):
        return op.mul(self, X)

    # Emmmm, How to say...
    def lshift(self, dt):
        return op.lshift(self, dt)

    # Delay signal
    def rshift(self, dt):
        return op.rshift(self, dt)

    def conv(self, X):
        return op.conv(self, X)
    
    def imp(self, seq='1', on='1', off='0'):
        return op.imp(self, seq=seq, on=on, off=off)
    
    def freeze(self, minT=10e-6, maxT=1000, sr = 44100):
        return op.freeze(self, minT=minT, maxT=maxT, sr = sr)

