import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp
import scipy.io
import scipy.fft
data3 = list(scipy.io.loadmat('H:/Materialy/korekta pasmowa/asynchr/takietam/RnCnF_mat.mat',squeeze_me=True).values())[3]
# metoda zobrazowania danych energetycznych przy definiowaniu wektora pobudzenia (a nie odpowiedzi)
nstart, nstop = int(710e3), int(715e3)
N = int(512e3)
n = np.arange(nstop-nstart) + nstart
nh = np.arange(nstop-nstart) + nstart - N
fig1 = plt.figure()
plt.plot(n,data3[n],n,data3[nh])
plt.gca().grid(True)
# obliczanie widma przebiegu odpowiedzi oraz przebiegu pobudzenia (bez eliminacji źródeł)
nstart, N, fp = int(710e3), int(32768), 51.2e3
n = np.arange(N) + nstart
nh = n - int(len(data3)/2)
Data2, Data3 = 20*np.log10(np.abs(scipy.fft.fft(data3[nh]))), 20*np.log10(np.abs(scipy.fft.fft(data3[n])))
f = np.linspace(0,fp-fp/N,N)
fig2 = plt.figure(figsize=(25,25))
plt.plot(f,Data2,f,Data3)
plt.gca().set_xlim(0,2000)
# obserwacja widma dowolnego fragmentu badanego przebiegu
fp=51.2e3
nstart, N = 0, 32768
n = np.arange(N)
data1 = data3[n]
f = np.linspace(0,fp-fp/N,N)
Data1 = np.abs(scipy.fft.fft(data1).real**2 + scipy.fft.fft(data1).imag**2)
fig3 = plt.figure()
plt.plot(f,20*np.log10(Data1),'ko')
plt.gca().set_xlim(0,2000)
plt.gca().grid(True)
