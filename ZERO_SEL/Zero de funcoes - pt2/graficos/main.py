import numpy as np
import matplotlib.pyplot as plt
from aprox_sem_print import bissec

#Exercícios do Tópico 2 Parte 2
#ia é o ponto inicial do intervalo
#ib é o ponto final do intervalo
#i2a é quando tem uma segunda raiz ela é usada como intervalo inicial para essa raiz
#i2b é quando tem uma segunda raiz ela é usada como intervalo final para essa raiz
#def f(x) = (È feito uma bissecção para achar onde esta a raiz e ficar um ponto vermelho no local)
#plt.plot = è usado para plotar os graficos

#ATENÇÂO!!!
#Os códigos foram comentando separando exercicio por exercio então para usar coloque um '#' antes das aspas (""")
#Exemplo ficando assim:  #""". Isso garante que quando rodar o codigo funcione e para comentar novamente só apague a '#'

"""
#Exemplo 2.1
ia = -0.2
ib = 0.2
i2a = 0.8
i2b = 1.0
# Geração dos pontos para o gráfico
def f(x): return (230 * (x**4) + 18 * (x**3) + 9 * (x**2) - 221 * x - 9)
x = np.linspace(ia, ib, 1000)
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = 230x^4 + 18x^3 + 9x^2 − 221x − 9')
#"""
#*********************//*********************
"""
#Exemplo 2.2
ia = 0.05
ib = 0.15
def f(x): return 20000*((x*((1+x)**6))/((1+x)**6 - 1)) - 4000
x = np.linspace(ia, ib, 1000)
plt.plot(x, f(x), '-', label='f(x) = 20000*((x*((1+x)**6))/((1+x)**6 - 1)) - 4000')
#"""
#*********************//*********************
"""
#Exemplo 2.3
ia = 0.1
ib = 1
def f(x): return ((np.pi * (x**2) * (3 - x)) / 3) - 0.5
x = np.linspace(ia, ib, 1000)
plt.plot(x, f(x), '-', label='V(H) = ((pi * H^2 * (3 * 1 - H)) / 3) - 0.5')
#"""
#*********************//*********************
"""
#Exemplo 2.4
ia = 0
ib = 5
def f(x): return (10 - 20 *(np.exp(-0.2*x) - np.exp(-0.75*x)) - 5)
x = np.linspace(ia, ib, 1000)
plt.plot(x, f(x), '-', label='10 - 20(exp(-0.2x) - exp(-0.75x)) - 5')
"""
#*********************//*********************
"""
#Exemplo 2.5
ia = 0
ib = 1
def f(x): return -8.12*(x**3) + 41.88*(x**2) - 71.99*x + 30.23
x = np.linspace(ia, ib, 1000)
plt.plot(x, f(x), '-', label='-8.12x^3 + 41.88x^2 - 71.99x + 30.23')
#"""

#*********************//*********************
(zero, k) = bissec(ia, ib, 10**-6, 10**-6, 100, f)
plt.plot(zero, f(zero), 'ro')

print(zero, f(zero))

if 'i2a' in locals():
  (zero, k) = bissec(i2a, i2b, 10**-6, 10**-6, 100, f)
  plt.plot(zero, f(zero), 'ro') 
#Adiciona a grade ao gráfico
plt.grid()

# Adicionar títulos e rótulos
plt.title('Gráfico da Função f(x)', fontweight='bold')
plt.xlabel('X', labelpad=8, fontsize=12, fontweight='bold')
plt.ylabel('Y', rotation=0, labelpad=20, fontsize=12, fontweight='bold')

# Adicionar legenda
plt.legend()

# Mostrar o gráfico
plt.show()
