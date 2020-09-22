import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp
import scipy.io
import scipy.fft
data3 = list(scipy.io.loadmat('H:/Materialy/korekta pasmowa/asynchr/takietam/RnCnF_mat.mat',squeeze_me=True).values())[3]
nstart, nstop, N = int(710e3), int(715e3), int(512e3)
nh = np.arange(nstop-nstart) + nstart - N
b,a = scp.butter(5,1000,fs=51.2e3,analog=False,btype='highpass')
w,h = scp.freqz(b,a)
fig1 = plt.figure()
plt.plot(w,20*np.log10(np.abs(h)))
y = scp.lfilter(b,a,data3[nh])
fig2 = plt.figure(figsize=(15,15))
plt.plot(nh,y)
plt.gca().set_xlim(199.9e3,200e3)
plt.gca().set_ylim(-0.0025,0.0025)
