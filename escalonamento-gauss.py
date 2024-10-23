import numpy as np

def gauss_elimination(matrix, vector, decimal_places=4):
    n = len(vector)
    augmented_matrix = np.column_stack((matrix, vector))  # Matriz aumentada [A|B]

    # Passo 1: Escalonamento
    print("Matriz aumentada inicial:")
    print(np.round(augmented_matrix, decimal_places))
    print()

    for i in range(n):
        # Escolha do pivô (diagonal principal)
        pivot = augmented_matrix[i][i]

        # Verificar se o pivô é zero (ou próximo) para evitar divisão por zero
        if np.isclose(pivot, 0):
            raise ValueError(f"Pivô nulo na linha {i}, reordene as equações!")

        # Normalizar a linha do pivô (deixar o pivô como 1)
        augmented_matrix[i] = augmented_matrix[i] / pivot
        augmented_matrix[i] = np.round(augmented_matrix[i], decimal_places)  # Arredondar a linha normalizada

        # Mostrar a matriz após normalização
        print(f"Iteração {i + 1}: Normalizar linha {i + 1}")
        print(np.round(augmented_matrix, decimal_places))
        print()

        # Eliminar as variáveis abaixo do pivô
        for j in range(i + 1, n):
            multiplier = augmented_matrix[j][i]  # Multiplicador
            augmented_matrix[j] -= multiplier * augmented_matrix[i]
            augmented_matrix[j] = np.round(augmented_matrix[j], decimal_places)  # Arredondar a linha ajustada

            # Mostrar a matriz após eliminação
            print(f"Iteração {i + 1}.{j}: Eliminar variável na linha {j + 1}")
            print(np.round(augmented_matrix, decimal_places))
            print()

    # Passo 2: Substituição regressiva
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solution[i] = augmented_matrix[i][-1] - np.dot(augmented_matrix[i][i + 1:n], solution[i + 1:n])
        solution[i] = np.round(solution[i], decimal_places)  # Arredondar a solução a cada passo

        # Mostrar solução parcial após cada iteração
        print(f"Substituição retroativa, solução parcial na iteração {n - i}:")
        print(np.round(solution, decimal_places))
        print()

    return solution


# Exemplo de uso:
A = np.array([[-4, 3, -1],
              [2, 4, -3],
              [2, -3, -1]], dtype=float)

B = np.array([5, 3, -1], dtype=float)

solucao = gauss_elimination(A, B, decimal_places=4)
print("Soluções finais: ", solucao)
