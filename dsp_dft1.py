import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp
import scipy.io
data = list(scipy.io.loadmat('G:/Czarny Pendrive/Szary Komputer/2/Doktorat/ss/ss/GIHA/Rejestracje/R1uF_mat.mat',squeeze_me=True).values())[3]
data = data-data.mean()
data = data/data.max()
n = np.arange(0,len(data),1)
b,a = scp.iirfilter(5,[0.05],btype='lowpass')  
y = scp.lfilter(b,a,data)
#fig = plt.figure(figsize=(20,20))
#plt.plot(n,data,'k',n,y,'b')
#plt.gca().set_xlim(160,1784)
#plt.gca().grid(True) 
N = 16384
data1 = data[0:N]
Data1 = scipy.fft(data1)
Data1 = np.sqrt(Data1.real**2+Data1.imag**2)*2/N
fp = 51.2e3
f = np.linspace(0,fp-fp/N,N)
plt.plot(f,20*np.log10(Data1),'ko')
plt.gca().set_xlim(0,500)
plt.gca().grid(True)
plt.gca().set_xlabel('f [Hz]')
plt.gca().set_ylabel(' Mag [dB]')
for k in [50,150,250,350,550]:
    plt.plot(np.array([k,k]),np.array([-140,0]),color='blue')
