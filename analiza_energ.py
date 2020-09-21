import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp
import scipy.io
data = list(scipy.io.loadmat('G:/Czarny Pendrive/Szary Komputer/2/Doktorat/ss/ss/GIHA/Rejestracje/R1uF_mat.mat',squeeze_me=True).values())[3]
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
plt.gca().set_xlim(0,2000)
plt.gca().grid(True)
plt.gca().set_xlabel('f [Hz]')
plt.gca().set_ylabel(' Mag [dB]')
for k in range(0,2000,50):
    plt.plot(np.array([k,k]),np.array([-140,0]),color='blue')
# wykreślanie sygnału zaburzenia    
start_point = 2e5
plt.figure(figsize=(5,5))
plt.plot(np.arange(0,N,1),data[np.arange(start_point,start_point+N,1,dtype='int')],'k')
plt.plot(np.arange(0,N,1),data[np.arange(start_point+int(512e3),start_point+N+512e3,1,dtype='int')],'b')
u = data[np.arange(start_point,start_point+N,1,dtype='int')]/data[np.arange(start_point,start_point+N,1,dtype='int')].max()
i = data[np.arange(start_point+int(512e3),start_point+N+512e3,1,dtype='int')]/data[np.arange(start_point+int(512e3),start_point+N+512e3,1,dtype='int')].max()
plt.figure()
# plt.plot(np.arange(0,N,1),i)
# plt.plot(np.arange(0,N,1),u)
I, U = np.abs( scipy.fft(i).real**2 + scipy.fft(i).imag**2 ), np.abs( scipy.fft(u).real**2 + scipy.fft(u).imag**2 )
plt.plot(f,20*np.log10(I),'bs',f,20*np.log10(U),'k*')
plt.gca().set_xlim(0,1000)
# impedancja
I, U = scipy.fft(i), scipy.fft(u)
Z = np.array(0)
for k in np.arange(0,2000,50,dtype='int')/(25/8):
    Z = np.append(Z,U[int(k)]/I[int(k)])
Z[2] = (Z[1]+Z[3])/2    # sztuczny zabieg
print(Z)    
print(abs(Z))
    
