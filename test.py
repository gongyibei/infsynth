from infsynth import *
from librosa import load


mapping = {
        'a': sin(440),
        's': sin(550),
        'd': squ(660),
        'f': squ(770),
        'g': saw(880),
        'h': saw(990),
        }

PolyKeySynth(mapping).start()
