# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(10,40,num=10, endpoint=True)

#Divisao (1/n)
y = [1/t for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq Convergente. -> ' r'$\lim_{x\rightarrow \infty} \frac{1}{n}$')

plt.axis((min(x) - 10, max(x)+5, 0.0001, 0.5))

#Gera o grafico final
plt.show()
