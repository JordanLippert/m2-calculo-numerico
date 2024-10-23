import numpy as np


# Função que será integrada
def f(x):
    return np.sin(x) ** 2 - 2 * x * np.sin(x) + 1


# Regra do Trapézio com impressão durante as iterações
def trapezio(a, b, n):
    h = (b - a) / n  # Tamanho do intervalo
    x = np.linspace(a, b, n + 1)  # Pontos entre a e b
    y = f(x)  # Valores de f(x) nesses pontos

    # Aplicando a fórmula do trapézio com prints intermediários
    I = (h / 2) * y[0]
    print(f"Iteração 0:")
    print(f"x[0] = {x[0]:.4f}, y[0] = {y[0]:.4f}, Contribuição: {(h / 2) * y[0]:.4f}")
    print(f"Soma parcial: {I:.4f}\n")

    for i in range(1, n):
        contrib = h * y[i]
        I += contrib
        print(f"Iteração {i}:")
        print(f"x[{i}] = {x[i]:.4f}, y[{i}] = {y[i]:.4f}, Contribuição: {contrib:.4f}")
        print(f"Soma parcial: {I:.4f}\n")

    I += (h / 2) * y[-1]
    print(f"Iteração {n}:")
    print(f"x[{n}] = {x[-1]:.4f}, y[{n}] = {y[-1]:.4f}, Contribuição: {(h / 2) * y[-1]:.4f}")
    print(f"Soma final: {I:.4f}\n")

    return I


# Parâmetros para o cálculo
a = 0.75  # Limite inferior
b = 1.75  # Limite superior
n = 8  # Número de trapézios

# Calculando a integral
resultado = trapezio(a, b, n)
print(f"O valor aproximado da integral é: {resultado:.4f}")
