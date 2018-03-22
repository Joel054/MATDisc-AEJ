# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(1,10,num=10, endpoint=True)

#Cálculo (n/(n+1))
y = [t/(t+1) for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq Limitada -> (an)=' r'$\frac{n}{n+1}$, tq 0<an<1')

plt.axis((0, max(x)+ 2, 0, 1))

#Gera o grafico final
plt.show()
