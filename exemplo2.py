# program texto.py
import matplotlib.pyplot as plt
from random import random
from math import sqrt

mu, sigma = 100, 15

x = list() 

for i in range(10000):
    u = random()-0.5
    if u >=0 :
    	x.append(mu + sigma*sqrt(u) )
    else:
    	x.append(mu - sigma*sqrt(-u))
            
    	# Desenha o histograma dos dados
        plt.hist(x, 50, normed=1, facecolor='g')
            
        plt.xlabel('ne'r'$\mathbb{N}$')
        plt.ylabel(r'$\mathbb{R}$')
        plt.title('Histograma do Teste')
        plt.text(95, .08, r'$\mu=100,\ \sigma=15$')
        plt.axis([85, 115, 0, 0.1])
        plt.grid(True)
        plt.show()
