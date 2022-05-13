# infsynth

infsynth



## tutorial

```python
from infsynth import *
```

使用 `sin`(正弦波）、 `squ`(方波）、`saw`(锯齿波)，生成基础波形。
```python
o = sin(440) # 生成440hz正弦波
```
使用 `+` 来叠加信号
```python
o = sin(440) + saw(440)
```
使用 `>>`(右移)、`<<`(左移) 来平移信号
```python
o = sin(440) >> 1 # 信号延迟1s
```

使用 `*` 调制幅度
```python
env = adsr() 
o = sin(440) * env
o = o * 0.9
```

频率调制
```python
# 生成频率周期性变化的信号
freq = saw(2) * 20 + 440 
o = sin(freq) 

```

mini techno
```python
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
