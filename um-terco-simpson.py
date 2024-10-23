import numpy as np


# Função a ser integrada (exemplo original)
def f(x):
    return 1 / (1 + x ** 2)


# Regra 1/3 de Simpson com impressão durante as iterações
def simpson_1_3(a, b, n, f):
    if n % 2 != 0:
        raise ValueError("n deve ser um número par.")

    h = (b - a) / n  # Tamanho do intervalo
    x = np.linspace(a, b, n + 1)  # Divisão do intervalo em n subintervalos
    y = f(x)  # Valores da função nos pontos

    # Inicializando as variáveis de soma
    I = (h / 3) * (y[0] + y[-1])
    soma_impares = 4 * sum(y[1:-1:2])
    soma_pares = 2 * sum(y[2:-1:2])

    # Print inicial (para x0 e xn)
    print(f"Iteração 0:")
    print(f"x[0] = {x[0]:.4f}, y[0] = {y[0]:.4f}")
    print(f"x[{n}] = {x[-1]:.4f}, y[{n}] = {y[-1]:.4f}")
    print(f"Soma inicial (y[0] + y[{n}]): {y[0] + y[-1]:.4f}\n")

    # Print dos termos ímpares
    print("Somas dos termos ímpares (multiplicados por 4):")
    for i in range(1, n, 2):
        print(f"x[{i}] = {x[i]:.4f}, y[{i}] = {y[i]:.4f}, Contribuição: {4 * y[i]:.4f}")
    print(f"Soma dos ímpares: {soma_impares:.4f}\n")

    # Print dos termos pares
    print("Somas dos termos pares (multiplicados por 2):")
    for i in range(2, n, 2):
        print(f"x[{i}] = {x[i]:.4f}, y[{i}] = {y[i]:.4f}, Contribuição: {2 * y[i]:.4f}")
    print(f"Soma dos pares: {soma_pares:.4f}\n")

    # Soma total
    I += (h / 3) * (soma_impares + soma_pares)

    # Resultado final
    print(f"Valor final da integral: {I:.6f}\n")

    return I


# Parâmetros para o cálculo de exemplo
a = 0  # Limite inferior
b = 1  # Limite superior
n = 2  # Número de subintervalos (deve ser par)

# Calculando a integral
resultado = simpson_1_3(a, b, n, f)
print(f"O valor aproximado da integral é: {resultado:.6f}")

# Agora, para os cálculos do volume e da área superficial da bola de futebol americano:

# Dados da tabela
z = np.array([0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0])  # z em cm
d = np.array([0, 6.6, 8.1, 12.2, 14.2, 15.2, 15.7, 15.2, 14.2, 12.2, 8.1, 6.6, 0])  # d em cm

# Calculando r(z) = d(z) / 2
r = d / 2


# Função para o volume (r^2) e área superficial (r)
def f_volume(z):
    return r ** 2


def f_area(z):
    return r


# Tamanho do intervalo h (assumindo intervalos igualmente espaçados)
h = z[1] - z[0]

# Cálculo do volume V (usando r(z)^2)
V = np.pi * simpson_1_3(z[0], z[-1], len(z) - 1, lambda z: r ** 2)

# Cálculo da área superficial S (usando r(z))
S = 2 * np.pi * simpson_1_3(z[0], z[-1], len(z) - 1, lambda z: r)

# Printando os resultados do volume e área superficial
print(f"Volume aproximado da bola: {V:.6f} cm³")
print(f"Área superficial aproximada da bola: {S:.6f} cm²")
