# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(1,10,num=10, endpoint=True)

#Divisao (1/n+1)
y = [1+(t/(t+1)) for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq Limitada Sup. -> ' r'$\lim_{x\rightarrow \infty} {1+} \frac{n}{n+1}$')

plt.axis((min(x) - 3, max(x)+3, 1.4, 2.01))

#Gera o grafico final
plt.show()
