import os
import math
from aprox import newtonRaphson, bissec, falsaPosicao
os.system('clear')

#Exercícios do Tópico 2 Parte 1
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
#Exercicio 1
ia = 1
ib = 2
ic = 1
def f(x): 
	return (x**2-3)
def f1(x):
	return 2*x
#"""
#*********************//*********************
"""
#Exemplo 2.1
#Exercicio 2
ia = 0.5
ib = 1
ic = 0.5
def f(x):
	return (x**2 + math.log(x))
def f1(x):
	return (2 * x + 1 / x)
#"""
#*********************//*********************
"""
#Exemplo 2.2
#Exercicio 1
ia = 0
ib = 1
ic = 0
def f(x):
	return (math.exp(-x) - math.sin(x))
def f1(x):
	return (-math.exp(-x) - math.cos(x))
#"""
#*********************//*********************
"""
#Exemplo 2.3
#Exercicio 1
ia = 2
ib = 3
ic = 3
def f(x):
	return (x*math.log(x) - 3.2)
def f1(x):
	return (math.log(x) + 1)
#"""
#*********************//*********************
"""
#Exemplo 2.4
#Exercicio 1
ia = -1
ib = 0
ic = -1
def f(x):
	return (math.cos(x) + x)
def f1(x):
	return (-math.sin(x) + 1)
#"""
#*********************//*********************
"""
#Exemplo 2.4
#Exercicio 2
ia = -1
ib = 0
ic = -1
def f(x):
	return (math.exp(x) + x)
def f1(x):
	return (math.exp(x) + 1)
#"""
#*********************//*********************
"""
#Exemplo 2.5
#Exercicio 1
ia = 1
ib = 3
ic = 3
def f(x):
	return (x**3 - 5)
def f1(x):
	return (3*x**2)
#"""
#*********************//*********************
"""
#Exemplo 2.5
#Exercicio 2
ia = -1
ib = 0
ic = -1
def f(x):
	return (x**3 - 5*x**2 + x + 3)
def f1(x):
	return (3*x**2 - 10*x + 1)
#"""
#*********************//*********************
"""
#Exemplo 2.6
#Exercicio 1
ia = 3
ib = 4
ic = 4
def f(x):
	return (math.sin(x) - math.tan(x))
def f1(x):
	return (math.cos(x) - (1 / math.cos(x)) ** 2) # 1/cos é a sec
#"""
#*********************//*********************
"""
#Exemplo 2.7
#Exercicio 1
ia = 1
ib = 2
ic = 2
def f(x):
	return (math.exp(-x**2) - math.cos(x))
def f1(x):
	return (-2*x*math.exp(-x**2) + math.sin(x))
#"""
#*********************//*********************
"""
#Exemplo 2.7
#Exercicio 2
ia = 1
ib = 2
ic = 1
def f(x):
	return (x**3 - x - 1)
def f1(x):
	return (3*x**2 - 1)
#"""
#*********************//*********************
"""
#Exemplo 2.7
#Exercicio 3
ia = 0
ib = 1
ic = 0
def f(x): return (4 * math.sin(x) - math.exp(x))
def f1(x): return (4 * math.cos(x) - math.exp(x))
#"""
#*********************//*********************

#Usando as funções:
#Nome_do_modo(Intervalo_inicial, Intervalo_final, epsoln1, epsoln2, Número_de_Interações, f(x), f'(x)
xm, k = bissec(ia, ib, 0.00001, 0.00001, 100, f)
print(f'\nAproximação {xm:.5f} à raiz, com', k, 'iterações\n')

xm, k = falsaPosicao(ia, ib, 0.00001, 0.00001, 100, f)
print(f'\nAproximação {xm:.5f} à raiz, com', k, 'iterações\n')

xm, k = newtonRaphson(ic, 0.00001, 0.00001, 100, f, f1)
print(f'\nAproximação {xm:.5f} à raiz, com', k, 'iterações\n')