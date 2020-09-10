# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:43:15 2020

@author: figonpiot
"""

# filtracja cyfrowa (DSP)
from matplotlib.pyplot import subplots, plot, xscale, xlim, show, close
from scipy.signal import firwin, chirp, lfilter
from numpy import linspace,pi,random
t = linspace(0,1,8001)
x = chirp(t,10,1,350,method='linear') + random.randn(8001)
b = firwin(32,0.1)
y = lfilter(b,1,x)

close()
# podstawowe nastawy dla wykresów
ax1 = plot(t,x,color='r')
ax2 = plot(t,y,color='k')
xscale("linear")
left, right = xlim()
xlim(left=0,right=0.5)




