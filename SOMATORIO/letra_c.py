# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import time


# Somatorio k=1 até n na geradora 1/(n+k)



def somatorio(n):    
    k = 2
    soma = 0
    ger = 0
    ini = 0
    fim = 0
    tempo = 0
    ini = time.time()
    print (ini)
    for k in range(1, n+1, 1):
        ger = 1/(k**2)
        #print ("k:")
        #print (k)
        #print ("Gerador:")
        #print (ger)
        soma += ger
        #print ("Somatorio:")
        #print (soma)
    fim = time.time()
    print(fim)
    tempo = fim - ini
    #print(tempo)
    #print (soma)
    return tempo


base = 10
i = 1
n = 0
for j in range(i, 10):
    n = base**i
    print ("\n Limite: ",n)
    print ("Tempo de Execucao:", somatorio(n), " segundos")
    i += 1
    



