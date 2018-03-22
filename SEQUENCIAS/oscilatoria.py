# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

#Num = é o numero de pontos que irá formar no gráfico
x = np.linspace(1,10,num=10, endpoint=True)

#Divisao (1/n+1)
y = [((-1/2)**t) for t in x]

plt.plot(x, y, 'ro')

#Label X
plt.xlabel('ne'r'$\mathbb{N}$')

#Label Y
plt.ylabel(r'$\mathbb{R}$')

#Titulo
plt.title('Seq Oscilatoria -> ' r'($ \frac{-1}{2}$)^n')
# plt.title('Seq finita. -> 5 Primeiros Termos tq (2^n)+1, n N* ')

plt.axis((min(x) - 3, max(x)+3, -3, 3))

#Gera o grafico final
plt.show()
