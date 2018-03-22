# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(1,10,num=10, endpoint=True)

#Cálculo (10^n + 1)
y = [(10**t)+1 for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq Limitada Inf.. -> (10^n)+1')

plt.axis((0, max(x)+ 2, 0, 1))

#Gera o grafico final
plt.show()
