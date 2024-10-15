# alturas = [1.80, 1.65, 1.72, 1.82, 1.91]

# media = sum([altura for altura in alturas]) / len(alturas)

# print(f"A média das alturas é {media:.2f} metros.")


# resultado_a = 0
# for x in range(2, 6):  # x vai de 2 a 5
#     for y in range(2, 4):  # y vai de 2 a 3
#         soma_parcial = (x + y) ** 2
#         resultado_a += soma_parcial
#         print(f"Para x={x}, y={y}: (x + y)^2 = {soma_parcial}")
        
# print(f"\nResultado do somatório a: {resultado_a}")


# numeros = []

# for i in range(5):
#     numero = float(input(f"Digite o {i + 1}º número: "))
#     numeros.append(numero)

# print("\nNúmeros na ordem inversa:")

# for i in range(5):
#     j = 4 - i  
#     print(f"Número {i + 1}: {numeros[j]}")


# import random

# num = []

# def sorteia():
#     for _ in range(6):
#         numero = random.randint(1, 100)
#         num.append(numero)
#     print(f"Números sorteados: {num}")

# def somaPar():
#     pares = [n for n in num if n % 2 == 0]
#     soma = sum(pares)
#     print("\nNúmeros pares sorteados:")
#     for par in pares:
#         print(f"Número par: {par}")
#     print(f"\nSoma dos números pares: {soma}")

# sorteia()
# somaPar()

# caracteres = []
# consoantes = []
# vogais = "aeiouAEIOU"
# quantidade_consoantes = 0

# for i in range(6):
#     caractere = input("Digite um caractere: ")
#     caracteres.append(caractere)
    
#     if caractere.isalpha() and caractere not in vogais:
#         quantidade_consoantes += 1
#         consoantes.append(caractere)

# print(f"Número de consoantes: {quantidade_consoantes}")
# print("Consoantes: {", " ".join(f"({c})" for c in consoantes), "}")

# notas = []
# medias = []
# alunos_acima_7 = 0

# for i in range(6):
#     soma = 0
#     print(f"Digite as 4 notas do aluno {i + 1}:")
    
#     for j in range(4):
#         nota = float(input(f"Nota {j + 1}: "))
#         soma += nota
    
#     media = soma / 4
#     medias.append(media)
    
#     if media >= 7.0:
#         alunos_acima_7 += 1

# print(f"Número de alunos com média maior ou igual a 7.0: {alunos_acima_7}")

# A = []
# soma_quadrados = 0

# for i in range(5):
#     num = int(input(f"Digite o número {i + 1}: "))
#     A.append(num)
#     soma_quadrados += num ** 2

# print(f"Soma dos quadrados dos elementos: {soma_quadrados}")

votos = [0] * 6
opcoes = ["Python", "C++", "Java", "Rust", "C#", "Outro"]
total_votos = 0

while True:
    voto = int(input("Qual a linguagem de programação com melhor tendência para o futuro? (1-6, 0 para encerrar): "))
    
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        votos[voto - 1] += 1
        total_votos += 1
    else:
        print("Voto inválido! Digite um número entre 1 e 6.")

print("\nLinguagem        Votos    %")
print("----------------------- ---- ----")

for i in range(6):
    percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
    print(f"{opcoes[i]:<15} {votos[i]:<7} {percentual:.0f}%")

print("----------------------- ----")
print(f"Total           {total_votos}")
