# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:07:56 2019

@author: Piotr
"""

from scipy import signal
import numpy as np
from math import pi
from matplotlib.pyplot import subplots
from matplotlib.pyplot import plot

b1 = signal.firwin(33,0.1);
b2 = signal.firwin(33,[0.1,0.2],pass_zero=False);
w1,h1 = signal.freqz(b1,1);
w2,h2 = signal.freqz(b2,1);
t = np.linspace(0,1,1001);
x = signal.chirp(t,f0=1,t1=1,f1=500/6,method='linear');
s = np.random.randn(1001)*0.05;
x = x+s;
y1 = signal.lfilter(b1,1,x);
y2 = signal.lfilter(b2,1,x);
fig, ax = subplots(2);
ax[0].plot(w1,20*np.log10(np.abs(h1)),color='tab:green');
ax[0].set_xlabel('w/2/pi');
ax[0].set_ylabel('|H(e(jw))|');
ax[0].grid(True);
ax[1].grid(True);
ax[1].plot(w2,20*np.log10(np.abs(h2)));
ax[1].set_xlabel('w/2/pi');
ax[1].set_ylabel('|H(e(jw))|');
fig1, ax=subplots(1);
ax.plot(t,y1,t,y2);
ax.set_xlabel('czas [s]');
ax.set_ylabel('y1[n],y2[n]');
ax.grid(True);
fig2, ax=subplots(1);
ax.plot(t,x,color='tab:blue')
ax.plot(np.array([np.min(t) ,np.max(t)]),np.array([1,1]),color='tab:red')
ax.plot(np.array([np.min(t) ,np.max(t)]),np.array([-1,-1]),color='tab:red')






