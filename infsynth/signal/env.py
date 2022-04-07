import numpy as np

from . import op
from .analog import AC, DC


class Attack(AC):
    def __init__(self, duration):
        AC.__init__(self, 1/duration)

    def oscillate(self, t):
        t = t%self.T
        return 1/self.T * t


class Decay(AC):
    def __init__(self, duration):
        AC.__init__(self, 1/duration)

    def oscillate(self, t):
        t = t%self.T
        return 1 - 1/self.T * t


Sustain = DC
Release = Decay


def ADSR(attack_time=0.01, decay_time=0.05, sustain_time=0.05, sustain_val=0.5, release_time=0.05):

    att = Attack(attack_time)
    dec = Decay(decay_time) * DC(1 - sustain_val) + DC(sustain_val)
    sus = Sustain(sustain_val)
    rel = Release(release_time) * DC(sustain_val)
    return op.concat([att, dec, sus, rel], [attack_time, decay_time, sustain_time, release_time])


# class ADSR(AC):
#     def __init__(self, freq, a, d, s, r):
#         AC.__init__(self, freq)
#         _sum = sum(a + d + s + r)
#         self.a = (a / _sum) * self.T
#         self.d = (d / _sum) * self.T
#         self.s = (s / _sum) * self.T
#         self.r = (r / _sum) * self.T

#     def oscillate(self, t):
#         t %= self.T
#         np.piecewise(
#             t,
#             [t < self.a],
#             [Attack(), Decay(), Sustain(), Release()]
#         )


# class AD(ADSR):
#     def __init__(self, freq, a, d):
#         ADSR.__init__(self, freq, a, d, 0, 0)


class AR(AC):
    pass
