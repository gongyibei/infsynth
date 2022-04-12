import math
from .analog import analog_warpper
from .basic import sin, squ, saw, dc
from . import op


# sin modulation
@analog_warpper
def sinm(freq):
    return (sin(freq) + 1.) * 0.5


# square modulation
@analog_warpper
def squm(freq):
    return (squ(freq) + 1.) * 0.5


# sawtooth modulation
@analog_warpper
def sawm(freq):
    return (saw(freq) + 1.) * 0.5


@analog_warpper
def attack(duration, curv=0.5):
    curv = min(max(curv, 1e-6), 1)
    exp = -math.log2(curv)
    return lambda t: ((t % duration) / duration)**exp


@analog_warpper
def decay(duration, curv=0.5):
    curv = min(max(1 - curv, 1e-6), 1)
    exp = -math.log2(curv)
    return lambda t: 1 - ((t % duration) / duration)**exp


@analog_warpper
def sustain(value):
    return lambda t: value


@analog_warpper
def release(duration, curv=0.5):
    curv = min(max(1 - curv, 1e-6), 1)
    exp = -math.log2(curv)
    return lambda t: 1 - ((t % duration) / duration)**exp


@analog_warpper
def adsr(attack_time=0.01,
         attack_curv=0.5,
         decay_time=0.05,
         decay_curv=0.3,
         sustain_time=0.05,
         sustain_val=0.5,
         release_time=0.5,
         release_curv=0.2
         ):
    att = attack(attack_time, attack_curv)
    dec = decay(decay_time, curv=decay_curv) * (1 - sustain_val) + sustain_val
    sus = sustain(sustain_val)
    rel = release(release_time, curv=release_curv) * sustain_val
    return op.concat([att, dec, sus, rel],
                     [attack_time, decay_time, sustain_time, release_time])

@analog_warpper
def ad(attack_time=0.01, decay_time=0.1, attack_curv=0.5, decay_curv=0.5):
    att = attack(attack_time, curv=attack_curv)
    dec = decay(decay_time, curv=decay_curv)
    return op.concat([att, dec],
                     [attack_time, decay_time]
                      )

    
