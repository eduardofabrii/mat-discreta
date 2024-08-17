# Exercicios da primeira lista de Python

A = {1,2,3,4,5,6}
print(A)

lista = ["bananas", "peras", "laranjas", "abacates"]
B = set(lista)
print(B)

lista = ["bananas", "peras", "laranjas", "limões", "bananas", "bananas", "abacates", "laranjas"]
B = set(lista)
print(B)

print(f'A cardinalidade do conjunto B = {B} é {len(B)}.')

A = {1,2,3,4,5}
print(A)

if (2 in A) :
    print('a)  2 ∈ A = VERDADEIRO')
    print(A)
else:
    print('a)  2 ∈ A = FALSO')

if (6 in A) :
    print('b) 6 ∈ A = VERDADEIRO')
    print(A)
else:
    print('b)  6 ∈ A = FALSO')

if (set() in A) :
    print('c) ∅ ∈ A = VERDADEIRO')
    print(A)
else:
    print('c) ∅ ∈ A = FALSO')


A = {1,2,3}
B = {3,2,1}

if (A == B) :
    print('Igual')
else:
    print('Falso')

# 7) Utilize a função issubset() para testar todos os subconjuntos de C = {2,3,4} – imprima os resultados

C = {2,3,4}

# print(A.issubset(C))?????








