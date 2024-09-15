import numpy as np
import matplotlib.pyplot as plt
from aprox_sem_print import bissec

#Exercícios do Tópico 2 Parte 1
#ia é o ponto inicial do intevalo
#ib é o ponto final
#def f(x) = (È feito uma bissecção para achar onde esta a raiz e ficar um ponto vermelho no local)
#plt.plot = è usado para plotar os graficos

#ATENÇÂO!!!
#Os códigos foram comentando separando exercicio por exercio então para usar coloque um '#' antes das aspas (""")
#Exemplo ficando assim:  #""". Isso garante que quando rodar o codigo funcione e para comentar novamente só apague a '#'

#"""
#Exemplo 2.1:
#Exercício 1.
ia = 1
ib = 2
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (x**2 - 3)
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = x^2 - 3')
#"""
#*********************//*********************
"""
#Exemplo 2.1:
#Exercício 2.
ia = 0.5
ib = 1
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (x**2 + np.log(x))
# Plot das funções
plt.plot(x, f(x), '-', label='g(x) = x^2 + ln(x)')
#"""
#*********************//*********************
"""
#Exemplo 2.2:
#Exercício 1.
ia = 0
ib = 1
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return np.exp(-x) - np.sin(x)
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = e^-x - sen(x)')
#"""
#*********************//*********************
"""
#Exemplo 2.3:
#Exercício 1.
ia = 2
ib = 3
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (x*np.log(x) - 3.2)
# Geração dos pontos para o gráfico
x = np.linspace(2, 3, 1000)
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = x*ln(x) - 3,2')
#"""
#*********************//*********************
"""
#Exemplo 2.4:
#Exercício 1.
ia = -1
ib = 0
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (np.cos(x) + x)
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = cos(x) + x')
#"""
#*********************//*********************
"""
#Exemplo 2.4:
#Exercício 2.
ia = -1
ib = 0
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (np.exp(x) + x)
# Plot das funções
plt.plot(x, f(x), '-', label='g(x) = e^x + x')
#"""
#*********************//*********************
"""
#Exemplo 2.5:
#Exercício 1.
ia = 1
ib = 3
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000) 
def f(x): return (x**3 - 5)
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = x^3 - 5')
#"""
#*********************//*********************
"""
#Exemplo 2.5:
#Exercício 2.
ia = -1
ib = 0
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (x**3 - 5*x**2 + x + 3)
# Plot das funções
plt.plot(x, f(x), '-', label='g(x) = x^3 - 5x^2 + x + 3')
#"""
#*********************//*********************
"""
#Exemplo 2.6:
#Exercício 1.
ia = 3
ib = 4
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (np.sin(x) - np.tan(x))
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = sen(x) - tg(x)')
#"""
#*********************//*********************
"""
#Exemplo 2.7:
#Exercício 1.
ia = 1
ib = 2
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (np.exp(-x**2) - np.cos(x))
# Plot das funções
plt.plot(x, f(x), '-', label='f(x) = e^(-x^2) - cos (x)')
#"""
#*********************//*********************
"""
#Exemplo 2.7:
#Exercício 2.
ia = 1
ib = 2
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (x**3 - x - 1)
# Plot das funções
plt.plot(x, f(x), '-', label='g(x) = x^3 - x - 1')
#"""
#*********************//*********************
"""
#Exemplo 2.7:
#Exercício 3.
ia = 0
ib = 1
# Geração dos pontos para o gráfico
x = np.linspace(ia, ib, 1000)
def f(x): return (4*np.sin(x) - np.exp(x))
# Plot das funções
plt.plot(x, f(x), '-', label='h(x) = 4*sen(x) - e^x')
#"""
#*********************//*********************



# Geração dos pontos para o gráfico
(zero, k) = bissec(ia, ib, 0.00001, 0.00001, 100, f)
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
