import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

def play(a, t=None, mint=1, maxt=10, sr=44100,):
    if t is None:
        t = a.T
        t = min(max(t, mint), maxt)

    t = np.arange(0, t, 1/sr)
    x = a(t)
    x = np.stack([x, x]).T
    sd.play(x, samplerate=sr)


def plot(a, t=1, sr=44100):
    t = np.arange(0, t, 1/sr)
    plt.plot(a(t))


# def loop(a, sr=44100):
#     play(a, t= )