import numpy as np
from itertools import permutations

def is_diagonally_dominant(A):
    """
    Verifica se a matriz A é diagonalmente dominante.
    Retorna True se for, e False se não for.
    """
    n = A.shape[0]
    for i in range(n):
        diag = abs(A[i, i])
        off_diag_sum = np.sum(np.abs(A[i, :])) - diag
        if diag <= off_diag_sum:
            return False  # Não é diagonalmente dominante
    return True


def make_diagonally_dominant(A, B):
    """
    Tenta reordenar a matriz A e o vetor B de forma que a matriz A
    se torne diagonalmente dominante. Retorna a nova matriz A e o vetor B
    ou levanta uma exceção se não for possível.
    """
    n = A.shape[0]
    # Tenta todas as permutações das linhas de A
    for perm in permutations(range(n)):
        A_permuted = A[list(perm), :]
        B_permuted = B[list(perm)]
        if is_diagonally_dominant(A_permuted):
            return A_permuted, B_permuted
    raise ValueError("Não foi possível reordenar a matriz para ser diagonalmente dominante.")


def gauss_seidel(A, B, tol=1e-3, max_iterations=100):
    # Tentar ajustar a matriz para torná-la diagonalmente dominante
    if not is_diagonally_dominant(A):
        print("Matriz não é diagonalmente dominante. Exibindo matriz original:")
        print(A)  # Imprime a matriz original
        A, B = make_diagonally_dominant(A, B)
        print("Matriz ajustada para ser diagonalmente dominante:")
        print(A)  # Imprime a matriz ajustada

    n = len(B)
    x = np.zeros_like(B)  # Inicializa o vetor x com zeros

    # Iterações
    for k in range(max_iterations):
        x_old = np.copy(x)

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])  # Somatório com valores já atualizados
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])  # Somatório com valores antigos
            x[i] = (B[i] - sum1 - sum2) / A[i, i]

        # Imprime o vetor solução a cada iteração
        print(f"Iteração {k + 1}: {x}")

        # Critério de parada: máxima diferença entre x_old e x
        if np.all(np.abs(x - x_old) < tol):
            print(f"Convergiu em {k + 1} iterações.")
            return x

    raise ValueError("O método de Gauss-Seidel não convergiu após o número máximo de iterações.")


# Matriz A e vetor B para o sistema de equações dado
A = np.array([[1, 10, 1, 0, 0, 0],
              [2, 0, 20, 1, 0, 0],
              [0, 3, 0, 0, 30, 3],
              [10, 0, 0, 1, 0, -1],
              [0, 0, 0, 5, -2, 20],
              [0, 0, 1, 10, -1, 0]], dtype=float)

B = np.array([10, 10, -15, 5, 5, 0], dtype=float)

# Chamada da função
try:
    solucao = gauss_seidel(A, B, tol=1e-3, max_iterations=20)
    print("Soluções: ", solucao)
except ValueError as e:
    print(e)
