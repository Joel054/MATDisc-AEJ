# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(1,7,num=7, endpoint=True)

#Cálculo (2^n + 1)
y = [(2**t)+1 for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq Limitada Inf.. -> (2^n)+1')

plt.axis((0, max(x)+ 2, 0, max(y)+10))

#Gera o grafico final
plt.show()
