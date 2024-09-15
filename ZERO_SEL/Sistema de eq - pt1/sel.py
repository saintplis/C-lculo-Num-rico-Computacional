def copy_2d(src, m, n):
    if n == 1:
        dest = [0.] * m
        for i in range(m):
            dest[i] = src[i]
        return dest

    dest = [([0.] * m) for _ in range(n)]

    for i in range(m):
        for j in range(n):
            dest[i][j] = src[i][j]

    return dest

def print_2d(A, n1, n2):
    for i in range(n1):
        print_1d(A[i], n2)
          
def print_1d(A, n1):
    for i in range(n1):
        if i == n1-1:
            print(f'{A[i]:4.6f}')
        else:
            print(f'{A[i]:4.6f}, ', end="")
              
def gauss(A, B):
    n = len(B)

    G = [([0] * n) for _ in range(n)]

    #copia da matriz para nao alterar a original
    G = copy_2d(A, n, n)
    P = copy_2d(B, n, 1)
    
    # Triangularização
    for k in range(n):
        for i in range(k+1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1, n):
                A[i][j] = A[i][j] - m * A[k][j]
            B[i] = B[i] - m * B[k]
    print('***Método de Gauss***\n')
    print('Matriz A original: ')
    print_2d(G, n, n)
    print('\nVetor B original: ')
    print_1d(P, n)
    print(f'Dimensao de n: {n}')
    print('\nMatriz triangularizada:')
    print_2d(A, n, n) 
    print('\nVetor B escalonado')
    print_1d(B, n)
  
    # Retrosubstituição
    X = [0] * n
    X[n-1] = B[n-1] / A[n-1][n-1]
    for k in range(n-1, -1, -1):
        soma = 0
        for j in range(k+1, n):
            soma += A[k][j] * X[j]
        X[k] = (B[k] - soma) / A[k][k]

    imprime_resultado(G, P, X, n)

def gauss_jacobi(A, B, ep, iter_max):
    print('\n***Método de Gauss-Jacobi***\n')
    n = len(B)
    X0 = [0] * n
    X = [0] * n
    iter_num = 1

    for iter_num in range(iter_max):
        for i in range(n):
            sum = 0
            for j in range(n):
                if i == j:
                    continue
                sum = sum + A[i][j] * X0[j]
            X[i] = (B[i] - sum) / A[i][i]
        val_max = pegar_valor_maximo_de_comp(X, X0, n)

        if val_max < ep:
            break

        X0 = copy_2d(X, n, 1) 

    print_gauss(A, B, n, iter_num)

    imprime_resultado(A, B, X0, n)

def gauss_seidel(A, B, ep, iter_max):
    print('***Método de Gauss-Seidel***\n')
    n = len(B)
    X0 = [0] * n
    X = [0] * n
    iter_num = 1

    for iter_num in range(iter_max):
        for i in range(n):
            sum = 0
            for j in range(n):
                if i == j:
                    continue
                sum = sum + A[i][j] * X[j]
            X[i] = (B[i] - sum) / A[i][i]
        val_max = pegar_valor_maximo_de_comp(X, X0, n)
        if val_max < ep:
            break
        X0 = copy_2d(X, n, 1) 
     
    print_gauss(A, B, n, iter_num)

    imprime_resultado(A, B, X0, n)
  
def print_gauss(A, B, n, iter_num):
    print('Matriz A original: ')
    print_2d(A, n, n)
    print('\nVetor B original: ')
    print_1d(B, n)
    print(f'\nDimensão n: {n}')
    print(f'\nNúmero de iterações: {iter_num}')


def lu(A, B):
    print('***Método de LU***\n')
    n = len(A)

    # Criar matriz N x N
    U = [([0.] * n) for _ in range(n)]
    L = [([0.] * n) for _ in range(n)]
    Y = [0.] * n
    X = [0.] * n

    # Cálculo dos elementos de L e U
    for i in range(n):
        for j in range(n):
            soma = 0
            for k in range(j):
                soma = soma + L[i][k] * U[k][j]
            if i <= j:
                U[i][j] = A[i][j] - soma
            else:
                L[i][j] = (A[i][j] - soma) / U[j][j]
    
    # Substituição progressiva (LY = B)
    for i in range(0, n):
        soma = 0
        for j in range(i):
            soma = soma + L[i][j] * Y[j]
        Y[i] = B[i] - soma
    
    # Substituição retroativa (UX = Y)
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma = soma + U[i][j] * X[j]
        X[i] = (Y[i] - soma) / U[i][i]
    
    print('Matriz A original: ')
    print_2d(A, n, n)
    print('\nVetor B original: ')
    print_1d(B, n)
    print('\nDimensão de n: %d' %n)
    print('\nFator L: ')
    print_2d(L, n, n)
    print('\nFator U: ')
    print_2d(U, n, n)
    print('\nSolução de Y para LY=B: ')
    print_1d(Y, n)
    imprime_resultado(A, B, X, n)

def thomas(A, B, C, D, MatrizOriginal):
    print('***Método de Thomas***\n')
    #copia os iniciais
    n = len(B)

    CC = copy_2d(C, n, 1)
    CD = copy_2d(D, n, 1)

    C[0] = C[0] / B[0]
    D[0] = D[0] / B[0]

    n = len(B)
  
    for i in range(1, n-1):
        denom = B[i] - A[i] * C[i-1]
        C[i] = C[i] / denom
        D[i] = (D[i] - A[i] * D[i-1]) / denom

    D[n-1] = (D[n-1] - A[n-1] * D[n-2]) / (B[n-1] - A[n-1] * C[n-2])
    
    X = [0.] * n
    X[n-1] = D[n-1]

    for i in range(n-2, -1, -1):
        X[i] = D[i] - C[i] * X[i+1]

    print('Vertores originais A, B, C e D: ')
    print('A: ', end='')
    print_1d(A, n)
    print('B: ', end='')
    print_1d(B, n)
    print('C: ', end='')
    print_1d(CC, n)
    print('D: ', end='')
    print_1d(CD, n)
    
    imprime_resultado(MatrizOriginal, CD, X, n)
    
# Função Auxiliar que pega o valor maximo entre X e X0 
def pegar_valor_maximo_de_comp(X, X0, n):
    max = abs(X[0] - X0[0])
    for i in range(1,n):
        val = abs(X[i] - X0[i])
        if val > max:
            max = val
    return max

def imprime_resultado(A, B, X, n):
    # Impressão da solução
    print('\nSolução X do sistema:')
    for x in X:
        print('%.6f' %x)
    
    print('\nVerificação dos resultados:')
    for x in range(n):
        for y in range(n):
            print('(%f * %f)' %(A[x][y],X[y]), end=" ")
            if y != n-1:
                print('+', end=" ")
            else:
                print('= %f' %B[x])
