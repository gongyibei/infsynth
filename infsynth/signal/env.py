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
def attack(duration):
    return lambda t: t

@analog_warpper
def decay(duration):
    return lambda t: 1 - t / duration

@analog_warpper
def sustain(value):
    return lambda t: value

@analog_warpper
def release(duration):
    return lambda t: 1 - t / duration

@analog_warpper
def adsr(attack_time=0.01, decay_time=0.05, sustain_time=0.05, sustain_val=0.5, release_time=0.05):
    att = attack(attack_time)
    dec = decay(decay_time) * (1 - sustain_val) + sustain_val
    sus = sustain(sustain_val)
    rel = release(release_time) * sustain_val
    return op.concat([att, dec, sus, rel], [attack_time, decay_time, sustain_time, release_time])