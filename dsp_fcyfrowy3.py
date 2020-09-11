# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:21:24 2020

@author: figonpiot
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as py
N = 1000
n = np.arange(0,N,1)
x = signal.chirp(n,0.001,N,0.003) + 0.1*np.random.randn(N)
b = signal.firwin(128,0.1)
b,a = signal.iirfilter(3,[0.1],btype='lowpass')          
y = signal.lfilter(b,a,x)
fig, ax = py.subplots(figsize=(10,10),dpi=80)
ax1 = py.subplot(211)
py.plot(n,x)
py.plot(n,y)
ax2 = py.subplot(212)
py.plot(n,y)
ax1.set_xlabel(' czas [s] ')
ax1.set_ylabel(' input [V] ')

ax1.legend(
    (ax1.lines),
    ('label1','label2'),
    loc='upper right')
