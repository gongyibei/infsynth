from infsynth import *
def bd(fs):
    freq = con(
    [ad(0.01, 0.1, 0.5, 0.2), dc(0)],
    [0.11, 0.39],) * 50 + 60
    env = con(
        [ad(0.01, 0.4, 0.5, 0.2), dc(0)],
        [0.41, 0.09],) 
    o = lpf(sin(freq), 60/fs) * env
    return o