# PODSTAWY NUMPY, CYFROWE PRZETWARZANIE SYGNAŁÓW
# tutorial_rozne1.py
praca z listami, zip, proste wykresy
------
# dsp_fcyfrowy1.py
proste wykresy, indywidualne importowanie procedur z bibliotek
------
# dsp_fcyfrowy2.py
projekt filtra cyfrowego
------
# dsp_fcyfrowy3.py
projekt filtra cyfrowego
------
# dsp_fcyfrowy4.py
# filtracja sygnału 50 Hz + silny szum / data = np.loadtxt('C:/Users/figonpiot/Desktop/siec_szum.txt') / filtrem rekursywnym dolnopasowym
# num_obliczenia_macierzowe1.py, różne działania na macierzach
------
# dsp_fcyfrowy_wektory
filtracja cyfrowa sygnału zmodulowanego częstotliwościowo zaszumionego, zwrócono uwagę na specyfikę (rozmiar wiersz. i kol.) wektorów dla funkcji lfilter z biblioteki scipy, z zamieszczeniem legendy do wykresu
------
# dsp_fcyfrowy2.py
implementacja filtra FIR oraz filtra IIR, z zamieszczeniem legendy do wykresu
------
# import_z_matpliku.py
jak w nazwie
# obliczanie koherencji.py (-wykresy)
wykreślanie funkcji koherencji dwóch przebiegów sin+szum, generowanie okna graficznego oraz osi liczbowej i jej konfiguracja (xlim,grid)
------
# dsp_dft1.py (html +)
obliczanie DFT sygnału znormalizowanego / list(scipy.io.loadmat('G:/Czarny Pendrive/Szary Komputer/2/Doktorat/ss/ss/GIHA/Rejestracje         /R1uF_mat.mat',squeeze_me=True).values())[3] /, wykres, obliczanie modułu widma, na końcu wydrukowanie amplitud poszczegolnych harmonicznych
for k in np.arange(0,2000,50,dtype='int')/(25/8):
    print(Data1[int(k)])
------    
# analiza_energ.py (html +)
rozszerzenie dsp_dft1.py, ten sam sygnał do analizy, wykreślanie pary u/i z dowolnie wybranego fragmentu sygnału, obliczanie dft u oraz i a nastepnie impedancji,
impedancje obliczono poprzez zastosowanie procedury np.append w petli (NP.APPEND)
# dane_energ_14_sygnalow.py 
14 sygnałów których źródłem była sieć energetyczna, krótki opis części z nich w środku pliku
------    
# analiza_energ1.py 
analiza sygnału /data3 = list(scipy.io.loadmat('H:/Materialy/korekta pasmowa/asynchr/takietam/RnCnF_mat.mat',squeeze_me=True).values())[3]/ 
1) metoda zobrazowania danych energetycznych przy definiowaniu wektora pobudzenia (a nie odpowiedzi, najpierw prad ulokowany bliżej końca ciągu, a następnie napięcie)
2) obliczanie widma przebiegu odpowiedzi oraz przebiegu pobudzenia (bez eliminacji źródeł)
3) obserwacja widma dowolnego fragmentu badanego przebiegu
zastosowano różne warianty wywołania NP.ARRANGE
