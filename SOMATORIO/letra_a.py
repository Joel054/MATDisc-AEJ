# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import timeit


# Somatorio k=1 até n na geradora 1/(n+k)
def somatorio(n):    
    i = 2
    soma = 0
    ger = 0
    for k in range(2, n + 1, 1):
        ger = 1/(n + i)        
        soma += ger        
        i +=1
    return soma


base = 10
for j in range(1, 6):    
    n = base**j
    ini = timeit.default_timer()
    print ("Somatorio: ", somatorio(n))
    fim = timeit.default_timer()
    print ("T(s): ", fim - ini)
    print ("\n")    
    

