matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

matriz_resultado= [
    #[0] para usar la fila en el lugar 0
    #sum para sumar la fila completa, probar sin append
    (matriz[0] + [sum(matriz[0])]),
    (matriz[1] + [sum(matriz[1])]),
    (matriz[2] + [sum(matriz[2])]),
    (matriz[3] + [sum(matriz[3])]),
]

print(matriz_resultado)

#usando insert con sum
matriz[0].insert(3,(sum(matriz[0]))),
#usando insert
matriz[1].insert(3,5),
#usando append
matriz[2].append(4),
#usando append con sum
matriz[3].append(sum(matriz[3]))

print(matriz)