import numpy as np
import matplotlib.pyplot as plt
N = 256
n = np.arange(256)
I = np.array( [ np.exp(-2*np.pi/N*k*n*1j) for k in range(256) ] )
f = 2
plt.plot(np.arange(N),I[f,:].real,'r',np.arange(N),I[f,:].imag,'k')
f = 254
plt.plot(np.arange(N),I[f,:].real,'g',np.arange(N),I[f,:].imag,'b')

x=np.sin(2*np.pi*100/256*n)
(I[100,:]*x).sum()
