# MATDisc-AEJ
Repositório para o projeto da cadeira de Matemática Discreta. Contribuição: Adriano Almeida, Everson Feltrin, Joel Ferreira da Si

## Desenvolvimento de trabalhos disciplina MATEMÁTICA DISCRETA 2018

### Trabalho 1 - Geração de Gráficos

* Linguagem Python
* SO Linux
* Biblioteca sugerida: matplotlib.pyplot
 

Primeiros Passos: É necessário ter instalado o módulo, para verificar se está instalado, basta digitar o comando python no terminal pra abrir o promp da linguagem no linux; No promp do python basta tentar importar a biblioteca, se não retornar nenhum erro, está correto.

Caso retorne erro, as bibliotecas necessárias são:
<blockquote>
<p>sudo apt-get install python-numpy</p>
<p>sudo apt-get install python-scipy</p>
<p>sudo apt-get install python-matplotlib </p>
 
</blockquote>
import matplotlib.pyplot as plt

Gerando exemplo 1:

<blockquote>
<p>plt.plot((1,2,3,4))</p>
<p>[<matplotlib.lines.Line2D object at 0x8fd48ac>] </p>
<p>plt.ylabel(u'Alguns Números')</p>
<p>plt.show() </p>
</blockquote>

Se tudo estiver correto, vai abrir uma janela com o gráfico.

Segue no repositório um documento com especificações do uso da library.



