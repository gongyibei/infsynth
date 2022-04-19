<div align="center">

# infsynth

<img width="200px" src="https://raw.githubusercontent.com/gongyibei/infsynth/master/logo.gif">

</div>

## tutorial

```python
from infsynth import *
import numpy as np
```

use `sin`、 `squ`、`saw` to generate basic signal

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

use `>>`、`<<` to delay signal

```python
o = sin(440) >> 1 # delay the signal 1 second
```

use `*` to modulate signal with envelope or reduce signal amplitude

```python
env = adsr() 
o = sin(440) * env
o = o * 0.9
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
t = np.array(0, duration, 1/sr) # Sampling time point
arr = o(t) # sampling the signal  
```


now! we can generate one music loop clip.
```python
fs = 44100
freq= concat(
    [ad(0.01, 0.1, 0.5, 0.1), dc(0)],
    [0.11, 1.89],
) * 50 + 60
bd_env = concat(
    [ad(0.01, 0.4, 0.5, 0.1), dc(0)],
    [0.41, 1.59],
)
bd = lpf(sin(freq), 60 / fs) * bd_env


lead_env = concat(
    [ad(0.01, 0.1), dc(0)],
    [0.11, 1.89]
)

bd = lpf(sin(freq)* bd_env, 60 / fs)
lead = lpf(saw(55)* lead_env * 0.1, 1000/fs) 

drum = imp(bd, '1111', T=2) *1.
melody = imp(lead, '1010 0010 1001 0010', T=2)
```
