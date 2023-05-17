respostas = []

while True:
    casos = int(input())

    if casos == 0:
        break        

    pedidos = []

    for i in range(casos):
        nome = input()
        cor, tamanho = input().split(" ")        
        pedidos.append([cor, tamanho, nome])
    
    # organiza primeiro a ultima coluna, por isso inicia no 2
    arrayIndex = 2

    def getArrayKey(array):
        global arrayIndex
        return array[arrayIndex]

    #converte pra lista pra usar o sort()
    pedidos = list(pedidos)

    #ultima coluna nomes
    pedidos.sort(key = getArrayKey)
    arrayIndex -= 1

    #penultima coluna P, M, G (ordem alfabetica reversa)
    pedidos.sort(reverse = True, key = getArrayKey)
    arrayIndex -= 1

    #primeira coluna
    pedidos.sort(key = getArrayKey)

    for i in pedidos:
        respostas.append(f"{i[0]} {i[1]} {i[2]}")
    respostas.append("")

respostas = respostas[:-1]
for r in respostas:
    print(r)