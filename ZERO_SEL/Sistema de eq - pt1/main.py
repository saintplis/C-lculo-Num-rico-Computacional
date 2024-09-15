from sel import gauss, gauss_seidel, gauss_jacobi, lu, thomas

#Tópico 3 Parte 1 
#Os exercícios foram separados 1 por 1 comentando cada um sendo assim para utilizar coloque um '#' antes das """
#Exemplo ficara assim '#""" '

#ATENÇÂO!!
#Os exercios do Exemplo 3.1 são usados 2 métodos Gauss e LU e somente funciona se usar um por vez então se usar o Gauss comente o LU colocando um '#' antes e vice-versa.
#Se for usado os 2 métodos ao mesmo tempo ira dar erro!!

#A = Matriz principal
#B = Resultado
#*********************//*********************
"""
#Exemplo 3.1
#Exercicio 1
A = [[1, 1, 1],
     [2, 1, -1],
     [2, 2, 1]]
B = [1, 0, 1]
gauss(A, B)
#lu(A, B)
#"""
#*********************//*********************
"""
#Exemplo 3.1
#Exercicio 2
A = [[1, 1, 1],
     [2, 1 ,-1],
     [2, -1, 1]]
B = [-2, 1, 3]
gauss(A, B)
#lu(A, B)
#"""
#*********************//*********************
"""
#Exemplo 3.1
#Exercicio 3
A = [[1, 10, 3],
     [0, 4 ,1],
     [2, 1, 4]]
B = [27, 6, 12]
gauss(A, B)
#lu(A, B)
#"""
#*********************//*********************
"""
#Exemplo 3.1
#Exercicio 4
A = [[0.1 , 0.2 ,  1  , 0.3],
     [0.3 , 2   , -0.3, -0.9],
     [4   , 2   , -0.3, 0.8],
     [0.6 , 3.2 , -1.8, 0.4]]
B = [4, 7.5, 4.4, 10]
gauss(A, B)
#lu(A, B)
#"""
#*********************//*********************
#A = Diagonal inferior 
#B = Diagonal Principal
#C = Diagonal Superior
#D = Resultado

"""
#Exemplo 3.2
#Exercicio 1
MatrizOriginal = [[20, -5, 0, 0],
                  [-5 ,15, -5, 0],
                  [0, -5, 15, -5],
                  [0, 0, -5, 19]]

A = [0, -5, -5, -5]
B = [20, 15, 15, 19]
C = [-5, -5, -5, 0]
D = [1100, 100, 100, 100]

thomas(A, B, C, D, MatrizOriginal)
#"""
#*********************//*********************
#"""
#Exemplo 3.2
#Exercicio 2
MatrizOriginal = [[3, -1, 0, 0],
                 [-1, 3, -1, 0],
                 [0, -1, 3, -1],
                 [0, 0, -1, 3]]

A = [0, -1, -1, -1]
B = [3, 3, 3, 3]
C = [-1, -1, -1, 0]
D = [2, 1, 1, 2]

thomas(A, B, C, D, MatrizOriginal)
#"""
#*********************//*********************
#Verifica os numeros das diagonais se eles são maiores que os numeros de sua linha. 
"""
#Exemplo 3.3
#Exercicio 1
A = [[10, 1, 1],
    [1, 5, 9],
    [2, 8, -4]]

A_permutada =  [[10, 1, 1],
               [2, 8, -4],
               [1, 5, 9]]

B = [12, 15, 6]

B_permutada = [12, 6, 15]
gauss_seidel(A_permutada, B_permutada, 10**-6, 100)
#gauss_jacobi(A_permutada, B_permutada, 10**-6, 100)
#"""
#*********************//*********************
"""
#Exemplo 3.3
#Exercicio 2
A = [[6, -1, 1],
    [1, 8, -1],
    [1, 1, 5]]
B = [7, 16, 18]
gauss_seidel(A, B, 10**-6, 100)
#gauss_jacobi(A, B, 10**-6, 100)
#"""
#*********************//*********************
"""
#Exemplo 3.3
#Exercicio 3
A = [[1, 10, 3],
    [4, 0, 1],
    [2, 1, 4]]
    
A_permutada = [[4, 0, 1],
               [1, 10, 3],
               [2, 1, 4]]
               
B = [27, 6, 12]

B_permutada = [6, 27, 12]
gauss_seidel(A_permutada, B_permutada, 10**-6, 100)
#gauss_jacobi(A_permutada, B_permutada, 10**-6, 100)
#"""
#*********************//*********************
"""
#Exemplo 3.3
#Exercicio 4
A = [[7, 1, -1],
    [1, 8, 1],
    [2, -1, 5]]
B = [13, 30, 12]
gauss_seidel(A, B, 10**-6, 100)
#gauss_jacobi(A, B, 10**-6, 100)
#"""
#*********************//*********************
"""
#Exemplo 3.3
#Exercicio 5
A = [[5, -1],
    [ 2, 4]]
B = [13, 14]
gauss_seidel(A, B, 10**-6, 100)
#gauss_jacobi(A, B, 10**-6, 100)
#"""
#*********************//*********************
"""
#Exemplo 3.3
#Exercicio 6
A = [[0.1, 0.2,    1,  0.3],
    [0.3 , 2  , -0.3, -0.9],
    [4   , 2  , -0.3,  0.8],
    [0.6 , 3.2, -1.8,  0.4]]

A_permutada =  [[4 ,   2, -0.3,  0.8],
               [0.6, 3.2, -1.8,  0.4],
               [0.1, 0.2,    1,  0.3],
               [0.3,   2, -0.3, -0.9]]

B = [4, 7.5, 4.4, 10]

A_permutada = [
    [4, 2, -0.3, 0.8],
    [0.6, 3.2, -1.8,  0.4],
    [0.1, 0.2, 1, 0.3],
    [0.3, 2 , -0.3, -0.9]]

B_permutada = [4.4, 10, 4, 7.5]
gauss_seidel(A_permutada, B_permutada, 10**-6, 100)
#gauss_jacobi(A_permutada, B_permutada, 10**-6, 100)
#"""