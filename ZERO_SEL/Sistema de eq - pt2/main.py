from sel import gauss, gauss_jacobi, gauss_seidel, lu
# PARTE IV

"""
# Exemplo 3.1
A = [[1, 10, 1],
     [9, 1, 0],
     [2, 2, 5]]
B = [170, 180, 140]

A_permutada = [[9, 1, 0],
               [1, 10, 1],
               [2, 2, 5]]
B_permutada = [180, 170, 140]

#Executar um método por vez
gauss(A, B)
#lu(A, B)
#gauss_jacobi(A_permutada, B_permutada, 10**-6, 100)
#gauss_seidel(A_permutada, B_permutada, 10**-6, 100)
"""

"""
# Exemplo 3.2
A = [[3, 4, 7, 20],
    [20, 25, 40, 50],
    [10, 15, 20, 22],
    [10, 8, 10, 15]]

B = [504, 1970, 970, 601]

#Executar um método por vez
#gauss(A, B)
#lu(A, B)
"""

#"""
# Exemplo 3.3
A = [[1, 1, 1],
     [0, 1, 2],
     [2, 1, 1]]
     
A_permutada = [[2, 1, 1],
               [1, 1, 1],
               [0, 1, 2]]

B = [12, 10, 16]
B_permutada = [16, 12, 10]
#Executar um método por vez
#gauss(A, B)
#lu(A, B)
gauss_seidel(A_permutada, B_permutada, 10**-6, 100)
#"""
