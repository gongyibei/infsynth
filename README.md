<div align="center">

<img width="200px" src="https://raw.githubusercontent.com/gongyibei/infsynth/master/logo.gif">

</div>

---

## tutorial

```python
from infsynth import *
import numpy as np
```

use `sin`, `squ` and `saw` to generate basic signal

```python
o = sin(440) # generate 440hz sine wave
o = squ(440) # generate 440hz square wave
o = saw(440) # generate 440hz sawtooth wave
```

the frequency of the basic signal could be an another signal varying with time.

```
freq = saw(2) * 20 + 440
o = sin(freq) 
```

use `+` to mix signals

```python
o = sin(440) + saw(440)
```

use `>>` and `<<` to shift signal

```python
o = sin(440) >> 1 # delay the signal 1 second
```

use `*` to modulate signal with envelope or reduce signal amplitude

```python
env = adsr() 
o = sin(440) * env
o = o * 0.9
```

use `lpf`,`hpf`,`lsf`,`hsf`,`bpf`,`bsf` and `pnf` to get basic filter effects

```python
# generate a bass drum loop
freq= ad([0.01, 0.1], [0.1, 0.1], T=2) * 50 + 60
bd_env = ad([0.01, 0.5], [0.4, 0.1], T=2)
bd = lpf(sin(freq)* bd_env, 100) # low-pass filter with 100hz cut-off frequency 
```

you can get the value of your signal any time point by calling the signal.

```python
val = o(np.pi) # get the value of your signal on 3.1415... second
```

you can use any sampling rate to sample your signal as follow:

```python
sr = 44100 # sampling rate
o = sin(440) # your signal
duration = 5 # sampling duration 
t = np.arange(0, duration, 1/sr) # Sampling time point
arr = o(t) # sampling the signal  
```

now! we can generate one music loop clip.

```python
freq= ad([0.01, 0.1], [0.1, 0.1], T=2) * 50 + 60
bd_env = ad([0.01, 0.5], [0.4, 0.1], T=2)
lead_env = ad(T=2)
bd = lpf(sin(freq)* bd_env, 100) 
lead = lpf(saw(50) * lead_env, 1000) * 0.1

drum = imp(bd, '1111')
melody = imp(lead, '1010 0010 1001 0010')
song = drum + melody

play(song, 10)
```
