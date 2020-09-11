# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:09:33 2020

@author: figonpiot
"""


import numpy as np
from scipy import signal
import matplotlib.pyplot as py
a = np.arange(0,10000,1)
x = signal.chirp(a,0.001,9999,0.003) + np.random.randn(10000)
b = signal.firwin(1288,0.1)
y = signal.lfilter(b,1,x)
fig, ax = py.subplots(figsize=(10,10))
ax1 = py.subplot(211)
py.plot(a,x)
ax2 = py.subplot(212)
py.plot(a,y)
print(a.shape)
print(x.shape)
print(b.shape)
print(y.shape)
