import os
import math
from aprox import newtonRaphson, bissec, falsaPosicao

#Exercícios do Tópico 2 Parte 2
#ia é o ponto inicial
#ib é o ponto final 
#ic é o ponto para usar em Newton-Raphson
#def f(x)  = (Coloque a função desejada)
#def f1(x) = (Derivada da função desejada)

#ATENÇÂO!!!
#Os códigos foram comentando separando exercicio por exercio então para usar coloque um '#' antes das aspas (""")
#Exemplo ficando assim:  #""". Isso garante que quando rodar o codigo funcione e para comentar novamente só apague a '#'

"""
#Exemplo 2.1
ia = -0.2
ib = 0.2
ic = -0.2
def f(x): return (230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9)
def f1(x): return (920*x**3 + 54*x**2 + 18*x - 221)
#"""
#*********************//*********************
"""
#Exemplo 2.2
ia = 0.05
ib = 0.15
ic = 0.05
def f(x): return 20000*((x*((1+x)**6))/((1+x)**6 - 1)) - 4000
def f1(x): return ((20000*(x**5 + 7*x**4 + 21*x**3 + 35*x**2 + 35*x + 21)*(1 + x)**5)/((x**5 + 6*x**4 + 15*x**3 + 20*x**2 + 15*x + 6)**2))
#"""
#*********************//*********************
"""
#Exemplo 2.3
ia = 0.1
ib = 1
ic = 1
def f(x): return ((math.pi * (x**2) * (3 * 1 - x)) / 3)-0.5
def f1(x): return (-math.pi*(-2 + x)*x)
#"""
#*********************//*********************
"""
#Exemplo 2.4
ia = 0
ib = 5
ic = 5
def f(x): return (10 - 20 *(math.exp(-0.2*x) - math.exp(-0.75*x)) - 5)
def f1(x): return (4*(math.exp(-0.2*x)) - 15*(math.exp(-0.75*x)))
#"""
#*********************//*********************
"""
#Exemplo 2.5
ia = 0
ib = 1
ic = 1
def f(x): return -8.12*(x**3) + 41.88*(x**2) - 71.99*x + 30.23
def f1(x): return -24.36*(x**2) + 83.76*x - 71.99
#"""

#*********************//*********************
#Usando as funções:
#Nome_do_modo(Intervalo_inicial, Intervalo_final, epsoln1, epsoln2, Número_de_Interações, f(x), f'(x)
xm, k = bissec(ia, ib, 10**-6, 10**-6, 100, f)
print(f'\nAproximação {xm:.6f} à raiz, com', k, 'iterações\n')

xm, k = falsaPosicao(ia, ib, 10**-6, 10**-6, 100, f)
print(f'\nAproximação {xm:.6f} à raiz, com', k, 'iterações\n')

xm, k = newtonRaphson(ic, 10**-6, 10**-6, 100, f, f1)
print(f'\nAproximação {xm:.6f} à raiz, com', k, 'iterações\n')