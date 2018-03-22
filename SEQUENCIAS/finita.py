# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(1,5,num=5, endpoint=True)

#Calculo
y = [(2**t)+1 for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq finita. -> 5 Primeiros Termos tq (2^n)+1, n N* ')

plt.axis((min(x)-min(x), max(x)+min(x), min(y) - min(y), max(y)+min(y)))

#Gera o grafico final
plt.show()
