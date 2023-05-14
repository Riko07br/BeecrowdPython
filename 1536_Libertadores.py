casos = int(input())

respostas = []

for i in range(casos):
    
    pontos = [0, 0]    

    jogo1 = input().strip(" ").split("x")    
    jogo1 = [int(i) for i in jogo1]

    if jogo1[0] > jogo1[1]:
        pontos[0] += 3
    elif jogo1[0] < jogo1[1]:
        pontos[1] += 3
    else:
        pontos[0] +=1
        pontos[1] +=1

    jogo2 = input().strip(" ").split("x")
    jogo2.reverse()
    jogo2 = [int(i) for i in jogo2]

    if jogo2[0] > jogo2[1]:
        pontos[0] += 3
    elif jogo2[0] < jogo2[1]:
        pontos[1] += 3
    else:
        pontos[0] +=1
        pontos[1] +=1
    
    saldo = [0, 0]
    saldo[0] = (jogo1[0] + jogo2[0]) - (jogo1[1] + jogo2[1])
    saldo[1] = (jogo1[1] + jogo2[1]) - (jogo1[0] + jogo2[0])
    
    if pontos[0] > pontos[1]:
        respostas.append("Time 1")
    elif pontos[0] < pontos[1]:
        respostas.append("Time 2")
    else:

        if saldo[0] > saldo[1]:
            respostas.append("Time 1")
        elif saldo[0] < saldo[1]:
            respostas.append("Time 2")
        else:

            if jogo2[0] > jogo1[1]:
                respostas.append("Time 1")
            elif jogo2[0] < jogo1[1]:
                respostas.append("Time 2")
            else:
                respostas.append("Penaltis")
    

for i in respostas:
    print(i)