from ordena import bubble, insertion_sort, selection_sort
import random


lista = []

print("Escolha uma opção de vetor")
print("1 - Aleatorio")
print("2 - Inverso Ordenado")
opc = input()

if(opc == '1'):
    for cont in range(0, 100):
        lista.append(random.randint(0, 20))
elif(opc == '2'):
    lista = list(range(100, 0, -1))


print("Escolha uma opção de ordenação")
print("1 - Selection Sort")
print("2 - Insertion Sort")
print("3 - Bubble Sort")
opc = input()

if(opc == '1'):
    selection_sort(lista)
elif(opc == '2'):
    insertion_sort(lista)
elif(opc == '3'):
    bubble(lista)


print(bubble(lista))
