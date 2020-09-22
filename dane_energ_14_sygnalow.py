# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:22:23 2020

@author: figonpiot
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as scp
import scipy.io

# dla komputer-laptop ścieżka 'H:\Materialy\korekta pasmowa\asynchr\takietam'

data1 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/RnCnF_mat.mat',squeeze_me=True).values())[3]
data2 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/RnCf_mat.mat',squeeze_me=True).values())[3]
data3 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/RNC5uFN_mat.mat',squeeze_me=True).values())[3]
data4 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/RNC1uFN_mat.mat',squeeze_me=True).values())[3]
data5 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/RNC5uFN_mat.mat',squeeze_me=True).values())[3]
data6 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/RC1unF_mat.mat',squeeze_me=True).values())[3]
data7 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/R5uF_mat.mat',squeeze_me=True).values())[3]
data8 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/R1uF_mat.mat',squeeze_me=True).values())[3]
data9 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/nRnCnF_mat.mat',squeeze_me=True).values())[3]
data10 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/nRncf_mat.mat',squeeze_me=True).values())[3]
data11 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/noR5uF_mat.mat',squeeze_me=True).values())[3]
data12 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Materialy/korekta pasmowa/asynchr/takietam/noR1uF_mat.mat',squeeze_me=True).values())[3]
data13 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Dane/Dane energetyczne/data_98.mat',squeeze_me=True).values())[3]
data14 = list(scipy.io.loadmat('G:/Dane do Stacjonarny WAT/dysk H/Dane/Dane energetyczne/data_97.mat',squeeze_me=True).values())[3]


# data3, data4, data5, data9 większe odkształcenie niż data1,data2
# data13 silny s.nieustalony, oscylacja
# data14 s.s.n, dużo artefaktów w sygnale

