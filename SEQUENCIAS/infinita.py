# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(1,5,num=10, endpoint=True)

#Divisao (1/n)
y = [2*(t**2) for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq infinita. -> 2^2-1')

plt.axis((min(x)-min(x), max(x)+min(x), min(y) - min(y), max(y)+min(y)))

#Gera o grafico final
plt.show()
