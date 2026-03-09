# 1. Crie uma lista chamada frutas com "maçã", "banana", "laranja". Imprima o segundo item.
frutas = ["maçã", "banana", "laranja"]
print("1.", frutas[1]) # O índice 1 representa o segundo item

# 2. Adicione "uva" no final da lista frutas e depois remova "banana". Imprima a lista.
frutas.append("uva")
frutas.remove("banana")
print("2.", frutas)

# 3. Crie uma lista vazia numeros. Usando um loop for, adicione os números de 1 a 10. Imprima o tamanho da lista.
numeros = []
for i in range(1, 11):
    numeros.append(i)
print("3. Tamanho da lista:", len(numeros))

# 4. Verifique se o número 7 está na lista numeros e imprima "Sim" ou "Não".
if 7 in numeros:
    print("4. Sim")
else:
    print("4. Não")

# 5. Use slicing para imprimir apenas os 3 primeiros itens da lista numeros. 
print("5.", numeros[:3])

# 6. Ordene a lista notas = [8.5, 7.0, 9.5, 6.0] do maior para o menor.
notas = [8.5, 7.0, 9.5, 6.0]
notas.sort(reverse=True)
print("6.", notas)

# 7. Conte quantas vezes o número 5 aparece na lista numeros.
print("7. O número 5 aparece", numeros.count(5), "vez(es).")

# 8. Inverta a lista numeros sem usar o método reverse().
# O fatiamento [::-1] lê a lista do início ao fim, mas com passo -1 (de trás para frente)
numeros_invertidos = numeros[::-1] 
print("8.", numeros_invertidos)

# 9. Crie uma nova lista com os quadrados dos números de 1 a 8 usando list comprehension.
quadrados = [x**2 for x in range(1, 9)]
print("9.", quadrados)

# 10. Dada palavras = ["python", "lista", "exercicio", "legal"], crie uma nova lista só com palavras que têm 5 letras ou mais.
palavras = ["python", "lista", "exercicio", "legal"]
palavras_longas = [p for p in palavras if len(p) >= 5]
print("10.", palavras_longas)




# 11. Junte as listas a=[1,2,3] e b=[4,5,6] em uma única lista.
a = [1, 2, 3]
b = [4, 5, 6]
lista_junta = a + b
print("11.", lista_junta)

# 12. Remova todos os números duplicados da lista [1, 2, 2, 3, 4, 4, 5] mantendo a ordem original. 
lista_com_duplicadas = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicadas = []
for numero in lista_com_duplicadas:
    if numero not in lista_sem_duplicadas:
        lista_sem_duplicadas.append(numero)
print("12.", lista_sem_duplicadas)

# 13. Escreva uma função que recebe uma lista e retorna o maior e o menor valor.
def maior_e_menor(lista):
    return max(lista), min(lista)

print("13. Maior e menor de [10, 20, 5]:", maior_e_menor([10, 20, 5]))

# 14. Crie uma matriz 2x3 (lista de listas) e imprima o elemento da linha 1, coluna 2.

matriz = [
    [10, 20, 30], 
    [40, 50, 60]
]
print("14. Elemento (linha 1, coluna 2):", matriz[0][1]) 

# 15. Faça uma cópia profunda de matriz=[[1,2],[3,4]], altere um valor na cópia e prove que a original não mudou (use copy). 
import copy

matriz_original = [[1, 2], [3, 4]]
matriz_copia = copy.deepcopy(matriz_original)


matriz_copia[0][0] = 99

print("15. Matriz Original:", matriz_original)
print("    Matriz Cópia:  ", matriz_copia)

# 16. Usando list comprehension, crie uma lista só com números pares entre 0 e 20. 
pares = [x for x in range(21) if x % 2 == 0]
print("16.", pares)

# 17. Escreva uma função que recebe duas listas e retorna True se elas tiverem os mesmos elementos (mesma quantidade e valores, sem considerar ordem). 
def listas_iguais(lista1, lista2):

    return sorted(lista1) == sorted(lista2)

print("17. As listas têm os mesmos elementos?", listas_iguais([1, 2, 3], [3, 1, 2]))

# 18. Crie uma lista de 10 números aleatórios (use random) e depois ordene apenas os números pares dessa lista.
import random

lista_aleatoria = [random.randint(1, 50) for _ in range(10)]
print("18. Lista aleatória original:", lista_aleatoria)

pares_ordenados = sorted([x for x in lista_aleatoria if x % 2 == 0])
print("    Apenas os pares ordenados:", pares_ordenados)

# 19. Remova da lista numeros todos os números menores que 5 sem criar uma nova lista.

numeros = [1, 8, 3, 9, 2, 7, 4, 6]

for i in range(len(numeros) - 1, -1, -1):
    if numeros[i] < 5:
        numeros.pop(i) 
print("19. Lista sem menores que 5:", numeros)

# 20. Escreva uma função que recebe uma lista de números e retorna uma nova lista com a soma acumulada (ex: [1,2,3] -> [1,3,6]).
def soma_acumulada(lista):
    
    acumulado = []
    soma = 0
    for num in lista:
        soma += num
        acumulado.append(soma)
    return acumulado

print("20. Soma acumulada de [1, 2, 3]:", soma_acumulada([1, 2, 3]))