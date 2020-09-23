# analiza sygnału elektroenergetycznego pobudzanego co 1.5 okresu
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp
import scipy.io
data = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/RNC5uFN_mat.mat',squeeze_me=True).values())[3]
# przeglądanie sygnału o długości 1 024 000 próbek , 1/2 napięcie , 1/2 prąd
# podobnie jak w pliku dsp_energ1.py 
nstart, nstop = int(750e3), int(760e3)
N = int(len(data)/2)
n = np.arange(nstop-nstart) + nstart           # prąd
nh = np.arange(nstop-nstart) + nstart - N      # napięcie
fig1 = plt.figure(figsize=(1,1))
plt.plot(n,data[n],n,data[nh])                 # wykres
plt.gca().grid(True)
# normalizacja 
nstart, nstop = int(0), int(512e3)
N = int(len(data)/2)
n = np.arange(nstop-nstart) + nstart
nh = np.arange(nstop-nstart) + nstart + N
data[n] = data[n]/data[n].max()                # normalizacja
data[nh] = data[nh]/data[nh].max()             # normalizacja
# wyświetlanie dwóch sygnałów do analizy 
# przeniesienie fragmentu przebiegu napiecia na strone pradu
nstartf, Nf = int(756e3), int(15360)
nendf = nstartf + Nf
nd = np.linspace(nstartf,nendf,Nf,dtype='int') # 15360 elementów 
fig1 = plt.figure(figsize=(10,10))
plt.plot(nh,data[nh],'y',nd,data[nd],'k.--',nd,data[nd-N]) # ostatnia para to napiecie przeniesione na strone i
plt.gca().grid(True)
plt.gca().set_xlim([nstartf, nstartf+Nf])
# przebiegi do analizy
data1 = data[nd]
data2 = data[nd-N]
# analiza częstotliwościowa
fp = 51.2e3
f = np.linspace(0,fp-fp/Nf,Nf)
Data1 = np.abs( scipy.fft(data1).real**2 + scipy.fft(data1).imag**2 )
Data2 = np.abs( scipy.fft(data2).real**2 + scipy.fft(data2).imag**2 )
plt.plot(f,20*np.log10(Data1),'ko-',f,20*np.log10(Data2),'b*')
plt.gca().set_xlim(0,200)
