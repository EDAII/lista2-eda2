import matplotlib.pyplot as plt 
import numpy as np


def selection_sort(lista):
    plt.ion()
    fig, ax = plt.subplots()
    x = range(0, len(lista))
    scatter_graph = ax.scatter(x, lista)

    for cont in range(len(lista)):
        index = cont
        for cont2 in range(cont+1, len(lista)):
            if lista[cont2] < lista[index]:
                index = cont2
        if index != cont:
            aux = lista[index]
            lista[index] = lista[cont]
            lista[cont] = aux

        scatter_graph.set_offsets(np.c_[x, lista])
        fig.canvas.draw_idle()
        plt.pause(0.1)

    plt.waitforbuttonpress()

    return lista


def insertion_sort(lista):
    plt.ion()
    fig, ax = plt.subplots()
    x = range(0, len(lista))
    scatter_graph = ax.scatter(x, lista)

    for cont in range(1, len(lista)):
        chave = lista[cont]

        aux = cont-1
        while (aux > -1) and chave < lista[aux]:
            lista[aux+1] = lista[aux]
            aux = aux-1
        lista[aux+1] = chave
        scatter_graph.set_offsets(np.c_[x, lista])
        fig.canvas.draw_idle()
        plt.pause(0.1)

    plt.waitforbuttonpress()

    return aux


def bubble(lista):
    plt.ion()
    fig, ax = plt.subplots()
    x = range(0, len(lista))
    scatter_graph = ax.scatter(x, lista)

    flag = True
    while (flag):
        flag = False
        for cont in range(0, len(lista)-1):
            if lista[cont] > lista[cont+1]:
                aux = lista[cont]
                lista[cont] = lista[cont+1]
                lista[cont+1] = aux
                flag = True

        scatter_graph.set_offsets(np.c_[x, lista])
        fig.canvas.draw_idle()
        plt.pause(0.1)

    plt.waitforbuttonpress()
