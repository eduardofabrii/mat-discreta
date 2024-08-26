# 1
import matplotlib.pyplot as plt
import numpy as np

# 2
def funcao1oGrau(a, b, x):
    return (a * x + b)

# 3
vetorX = np.arange(-5, 5, 0.01)
print("VetorX: ", vetorX)

# 4
a = 4
b = 2
vetorY = funcao1oGrau(a, b, vetorX)
print("VetorY: ", vetorY)

# 5
# Criando janela da figura
fig = plt.figure(figsize=(10, 10))
# Plotando ponto a ponto do vetor x com o respectivo y
plt.plot(vetorX, vetorY, label = "Função do 1° Grau")
# Chamando função para abrir janela
plt.show()

# 6
fig = plt.figure(figsize=(10, 10))
plt.plot(vetorX, vetorY, label="Função do 1° Grau")
plt.title('f(x) = ax + b')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()

# 7. a)
def funcao2oGrau(a, b, c, x):
    return a * x**2 + b * x + c

vetorX = np.arange(-10, 10, 0.01)
vetorY = funcao2oGrau(10, 232, 54, vetorX)

fig = plt.figure(figsize=(10, 10))
plt.scatter(vetorX, vetorY, label="Função do 2° Grau")
plt.title('f(x) = ax² + bx + c')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()


# 7. b)
def funcaoExponencial(a, b, x):
    return a * b**x

vetorX = np.arange(-2, 2, 0.001)
vetorY = funcaoExponencial(2, 1.5, vetorX)

fig = plt.figure(figsize=(10, 10))
plt.scatter(vetorX, vetorY, label="Função Exponencial")
plt.title('f(x) = a * b^x')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()

# 7. c)
def funcaoModular(x):
    return np.abs(x)

vetorX = np.arange(-10, 10, 0.01)
vetorY = funcaoModular(vetorX)

fig = plt.figure(figsize=(10, 10))
plt.scatter(vetorX, vetorY, label="Função Modular")
plt.title('f(x) = |x|')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()

# 7. d)
def funcaoSeno(x):
    return np.sin(x)

vetorX = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
vetorY = funcaoSeno(vetorX)

fig = plt.figure(figsize=(10, 10))
plt.scatter(vetorX, vetorY, label="Função Seno")
plt.title('f(x) = sen(x)')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()
plt.grid(True, which='both')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()


