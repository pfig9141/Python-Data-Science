# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:54:47 2020

@author: figonpiot
"""
####
## wagi
#w1,w2,w3 = 0.2,0.3,0.5
## dane atmosferyczne
#kanto = [73, 67, 43]
#johto = [91, 88, 64]
#hoenn = [87, 134, 58]
#sinnoh = [102, 43, 37]
#unova = [69, 96, 70]
## utworzenie listy z wartosciami liczbowymi wag
#weights = [w1,w2,w3]
####
#
#
#kanto = [1,1,1]
#johto = [1,2,3]    
#result = 0
#for x,w in zip(kanto,johto):
#    result += x * w
#    print(result)
#    
#import numpy as np
#x = np.arange(0,2*np.pi,2*np.pi/100)
#arr1 = np.sin(2*np.pi*1*x)
#arr2 = np.cos(2*np.pi*1*x)
#arr3 = np.exp(-x)
#
#result = 0
#for a,b,c in zip(arr1,arr2,arr3):
#    result += a * b * c 
#    print(result)
    
# listy    
#lista = [1,2,3]
#lista.append(4)     # dodaje element do listy [1,2,3,4]
#lista.extend([0,0]) # dodaje listę do listy
#lista.insert(0,-1)  # dodaje wartosc 1 na pozycji 0
## lista.pop(0)
# 
## usuwa wszystkie elementy z listy 
#lista =[1,2,3,4,5,6]
#N = 5
#for k in range(0,6): lista.pop(N-k)
#    
#lista =[-1,-2,3,-4,5,6]
#for k in zip(lista):
#    lista.remove(k)
#    

## wykreślanie wykresu
#from matplotlib import pyplot
#import numpy as np
#lista = []					# wcześniejsze wyzerowanie listy
## for k in range(0,1000): lista.append(random()) 	# losowanie 1000 liczb
## arr = np.array(lista)			  	# konwersja do np-tablicy
#arr = np.random.randn(1,1000)       # lub za pomocą numpy
#pyplot.plot(np.arange(0,1000,1).reshape(1000,1),arr.reshape(1000,1),
#            color='green',marker='o',linestyle='solid')
#np.savetxt('my_results.txt',arr,fmt ='%.2f',comments='')
# pyplot.subplots() # generuje os liczbowa


